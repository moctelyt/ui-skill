import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]
SKILL=BASE/'.agents'/'skills'/'ui-design-director'
SCRIPTS=SKILL/'scripts'

class SkillTests(unittest.TestCase):
    def test_skill_frontmatter_and_references(self):
        text=(SKILL/'SKILL.md').read_text()
        self.assertTrue(text.startswith('---\nname: ui-design-director\n'))
        self.assertIn('description:',text)
        for path in ['references/style-catalog.json','references/theme-recipes.json','references/selection-framework.md','references/design-standards.md']:
            self.assertTrue((SKILL/path).is_file(),path)

    def test_catalog_has_220_unique_entries(self):
        data=json.loads((SKILL/'references/style-catalog.json').read_text())
        self.assertEqual(len(data['styles']),220)
        self.assertEqual(len({x['slug'] for x in data['styles']}),220)
        self.assertEqual(len({x['category'] for x in data['styles']}),10)

    def test_theme_recipes_have_32_entries(self):
        data=json.loads((SKILL/'references/theme-recipes.json').read_text())
        self.assertEqual(len(data['recipes']),32)

    def test_validation_passes(self):
        p=subprocess.run([sys.executable,str(SCRIPTS/'validate_catalog.py')],capture_output=True,text=True)
        self.assertEqual(p.returncode,0,p.stderr)

    def test_recommendation_for_chat(self):
        p=subprocess.run([sys.executable,str(SCRIPTS/'recommend.py'),'--project','AI chat assistant dashboard','--mood','premium dark','--top','3','--json'],capture_output=True,text=True)
        self.assertEqual(p.returncode,0,p.stderr)
        candidates=json.loads(p.stdout)
        self.assertEqual(len(candidates),3)
        self.assertIn('aurora-ai',[r['id'] for r in candidates])

    def test_tokens_and_non_overwrite(self):
        with tempfile.TemporaryDirectory() as td:
            target=Path(td)/'theme.css'
            args=[sys.executable,str(SCRIPTS/'theme_tokens.py'),'--recipe','quiet-enterprise','--output',str(target)]
            p=subprocess.run(args,capture_output=True,text=True)
            self.assertEqual(p.returncode,0,p.stderr)
            self.assertIn('--ui-on-accent:',target.read_text())
            p2=subprocess.run(args,capture_output=True,text=True)
            self.assertNotEqual(p2.returncode,0)

    def test_installer_non_destructive_and_idempotent_hints(self):
        with tempfile.TemporaryDirectory() as td:
            repo=Path(td)
            (repo/'AGENTS.md').write_text('# Existing instructions\nRespect security rules.\n')
            args=[sys.executable,str(BASE/'install.py'),'--target',str(repo),'--with-hints']
            p=subprocess.run(args,capture_output=True,text=True)
            self.assertEqual(p.returncode,0,p.stderr)
            installed=repo/'.agents/skills/ui-design-director/SKILL.md'
            self.assertTrue(installed.is_file())
            updated=(repo/'AGENTS.md').read_text()
            self.assertIn('Respect security rules.',updated)
            self.assertEqual(updated.count('<!-- ui-design-director:start -->'),1)
            again=subprocess.run(args,capture_output=True,text=True)
            self.assertNotEqual(again.returncode,0)
            overwrite=subprocess.run(args+['--force'],capture_output=True,text=True)
            self.assertEqual(overwrite.returncode,0,overwrite.stderr)
            self.assertEqual((repo/'AGENTS.md').read_text().count('<!-- ui-design-director:start -->'),1)
            self.assertTrue(any(x.name.startswith('ui-design-director.backup-') for x in (repo/'.agents/skills').iterdir()))

    def test_global_installer_targets_two_personal_locations(self):
        with tempfile.TemporaryDirectory() as td:
            args=[sys.executable,str(BASE/'install.py'),'--scope','global','--home',td]
            result=subprocess.run(args,capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
            home=Path(td)
            self.assertTrue((home/'.agents/skills/ui-design-director/SKILL.md').is_file())
            self.assertTrue((home/'.gemini/config/skills/ui-design-director/SKILL.md').is_file())
            self.assertFalse((home/'AGENTS.md').exists())

    def test_explorer_embedded_data(self):
        html=(BASE/'explorer/index.html').read_text()
        self.assertIn('skill-data',html)
        self.assertIn('Floating Glass',html)
        self.assertIn('220',html)

if __name__=='__main__':unittest.main()
