#!/usr/bin/env python3
"""Safely install the shared UI design skill per project or for all local workspaces."""
import argparse
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

NAME='ui-design-director'
START='<!-- ui-design-director:start -->'
END='<!-- ui-design-director:end -->'
HINT = f'''{START}
## UI Design Director (frontend tasks only)
When a developer starts a new frontend, website, landing page, dashboard, app UI or explicit visual redesign, consider the **ui-design-director** skill from `.agents/skills/ui-design-director/SKILL.md` before coding. Inspect the existing project and brand first. When the new design direction is unspecified and materially affects the result, offer up to **three tailored UI directions**, with tradeoffs, and ask one concise choice (or let the developer delegate selection). When an established design system exists, preserve it by default. Do not raise style questions for backend-only tasks, bug fixes or explicitly styled work. The skill is a recommendation workflow, not authorization for unrequested changes.
{END}
'''

def add_hint(path,dry_run=False):
    existing=path.read_text(encoding='utf-8') if path.exists() else ''
    if START in existing and END in existing:
        before,rest=existing.split(START,1)
        _,after=rest.split(END,1)
        new=before+HINT+after
        action='refresh'
    elif START in existing or END in existing:
        raise ValueError(f'Incomplete existing UI skill markers in {path}; refusing modification')
    else:
        new=existing.rstrip()+'\n\n'+HINT if existing.strip() else HINT
        action='append'
    if new==existing: return 'unchanged'
    if not dry_run:
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(new,encoding='utf-8')
    return action

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scope',choices=['project','global'],default='project',help='project: repository; global: both common user-skill folders')
    parser.add_argument('--target',default='.',help='Target repo root for --scope project; default current folder')
    parser.add_argument('--home',default=None,help=argparse.SUPPRESS)  # For test isolation / advanced users
    parser.add_argument('--with-hints',action='store_true',help='Project only: add brief UI trigger hints to AGENTS.md and .github/copilot-instructions.md')
    parser.add_argument('--force',action='store_true',help='Back up and replace an existing skill folder')
    parser.add_argument('--dry-run',action='store_true',help='Preview actions without writing files')
    args=parser.parse_args()
    if args.scope=='global' and args.with_hints:
        parser.error('--with-hints is project-only; always-on AGENTS.md is intentionally repo-scoped')
    if args.scope=='project' and args.home:
        parser.error('--home is only applicable to --scope global')
    source=Path(__file__).resolve().parent/'.agents'/'skills'/NAME
    if not (source/'SKILL.md').is_file():
        parser.error('Source skill is missing from this package')
    if args.scope=='project':
        root=Path(args.target).expanduser().resolve()
        if not root.is_dir(): parser.error(f'Target is not a folder: {root}')
        destinations=[root/'.agents'/'skills'/NAME]
    else:
        home=Path(args.home).expanduser().resolve() if args.home else Path.home()
        if not home.is_dir(): parser.error(f'Home folder does not exist: {home}')
        destinations=[home/'.agents'/'skills'/NAME, home/'.gemini'/'config'/'skills'/NAME]
    for destination in destinations:
        if destination.resolve()==source.resolve():
            parser.error('Install destination cannot be the package source')
        if destination.exists() and not args.force:
            parser.error(f'{destination} already exists. Use --force to back it up and replace it.')
    for destination in destinations:
        print(f'Install skill: {destination}')
        if destination.exists():
            suffix=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
            backup=destination.parent/f'{NAME}.backup-{suffix}'
            n=1
            while backup.exists():
                n+=1; backup=destination.parent/f'{NAME}.backup-{suffix}-{n}'
            print(f'Backup existing skill: {backup}')
            if not args.dry_run: destination.rename(backup)
        if not args.dry_run:
            destination.parent.mkdir(parents=True,exist_ok=True)
            shutil.copytree(source,destination)
    if args.with_hints:
        for p in (root/'AGENTS.md',root/'.github'/'copilot-instructions.md'):
            print(f'{add_hint(p,args.dry_run)} trigger hint: {p}')
    print('Done.' if not args.dry_run else 'Dry run complete; no files were changed.')
    print('Restart/reopen your agent session if it does not discover newly installed skills.')
    return 0

if __name__=='__main__': sys.exit(main())
