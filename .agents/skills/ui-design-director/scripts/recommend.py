#!/usr/bin/env python3
"""Suggest offline UI design recipes; heuristic, not predictive and never auto-edits files."""
import argparse
import json
import re
from pathlib import Path

RECIPES = Path(__file__).resolve().parents[1] / 'references' / 'theme-recipes.json'
ALIASES = {
 'artificial intelligence': 'ai assistant agent chat', 'agentic': 'agent ai',
 'chatbot': 'chat ai assistant', 'llm': 'ai chat assistant',
 'website': 'landing product marketing', 'webapp': 'saas app', 'web app': 'saas app',
 'copilot': 'ai assistant developer', 'crm': 'crm dashboard saas',
 'developer tools': 'developer devtools sdk api', 'school': 'education learning',
 'nursery': 'kids children education', 'kindergarten': 'kids education',
 'storefront': 'ecommerce retail shop', 'shopify': 'ecommerce retail shop',
 'payment': 'fintech finance payments', 'banking': 'fintech finance bank',
 'portfolio': 'portfolio creative', 'agency': 'agency marketing services',
 'dashboard': 'dashboard analytics admin', 'internal': 'admin enterprise',
 'news': 'news publisher article', 'blog': 'blog news article',
 'game': 'gaming esports', 'travel': 'travel hotel booking',
 'hospital': 'healthcare medical hospital', 'mobile': 'mobile app',
 'android': 'android mobile', 'ar/vr': 'ar vr spatial',
 'workflow': 'agent operations productivity', 'automation': 'agent operations productivity',
}

def tokens(value):
    return set(re.findall(r'[a-z0-9]+', value.lower()))

def expanded_tokens(value):
    result = tokens(value)
    lower = value.lower()
    for key, more in ALIASES.items():
        if key in lower:
            result.update(tokens(more))
    return result

def rank(project, mood='', excluded=(), limit=3):
    data = json.loads(RECIPES.read_text(encoding='utf-8'))['recipes']
    p, m = expanded_tokens(project), expanded_tokens(mood)
    exclusions = set(excluded)
    ranked = []
    for recipe in data:
        if recipe['id'] in exclusions:
            continue
        tags = set(recipe['tags'])
        moods = set(recipe['moods'])
        names = tokens(recipe['name'] + ' ' + recipe['best_for'])
        score = 7 * len(p & tags) + 3 * len(p & names) + 6 * len(m & moods) + 1 * len(p & moods)
        if 'dark' in m and recipe['palette']['bg'].upper() not in ('#090C18','#0B0A19','#10151A','#101522','#11100F','#111A23','#181B1E','#190C31','#1C1C1E'):
            score -= 5
        if 'light' in m and recipe['id'] in ('aurora-ai','data-operations','dark-luxury','cyber-esports','vaporwave-creator','developer-terminal','spatial-experience'):
            score -= 5
        ranked.append((score,recipe))
    ranked.sort(key=lambda p: (-p[0],p[1]['priority']))
    return ranked[:min(limit, len(ranked))]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', required=True, help='Product description, e.g. "AI chat SaaS dashboard"')
    parser.add_argument('--mood', default='', help='Optional direction, e.g. "premium dark"')
    parser.add_argument('--top', type=int, default=3, help='Number of options, 1–10 (default: 3)')
    parser.add_argument('--exclude', default='', help='Comma-separated recipe IDs to exclude')
    parser.add_argument('--json', action='store_true', help='Machine-readable output')
    args = parser.parse_args()
    if not 1 <= args.top <= 10:
        parser.error('--top must be from 1 to 10')
    results = rank(args.project,args.mood,[s.strip() for s in args.exclude.split(',') if s.strip()],args.top)
    if args.json:
        print(json.dumps([{'rank':i, 'heuristic_score':score, **recipe} for i,(score,recipe) in enumerate(results,1)],indent=2))
    else:
        print('Suggested UI directions (offline keyword heuristic; inspect project before implementation):')
        for i,(score,r) in enumerate(results,1):
            p=r['palette']
            print(f"\n{i}. {r['name']} [{r['id']}] — relevance score {score}")
            print(f"   Use case: {r['best_for']}")
            print(f"   Mix: {r['style_mix']}")
            print(f"   Colors: bg {p['bg']}, surface {p['surface']}, text {p['text']}, accent {p['accent']}")
            print(f"   Layout: {r['layout']}")
        print('\nNot a substitute for project context, user choice, or contrast testing.')

if __name__ == '__main__':
    main()
