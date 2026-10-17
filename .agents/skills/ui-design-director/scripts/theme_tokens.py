#!/usr/bin/env python3
"""Produce a starter CSS token sheet for a selected theme recipe."""
import argparse
import json
from pathlib import Path

CATALOG = Path(__file__).resolve().parents[1] / 'references' / 'theme-recipes.json'

def as_rgb(s):
    h = s.lstrip('#')
    return tuple(int(h[i:i+2],16) for i in (0,2,4))

def luminance(color):
    rgb = [x/255 for x in as_rgb(color)]
    rgb = [x/12.92 if x <= .04045 else ((x+.055)/1.055)**2.4 for x in rgb]
    return rgb[0]*.2126 + rgb[1]*.7152 + rgb[2]*.0722

def contrast(c1,c2):
    l1,l2 = sorted([luminance(c1),luminance(c2)],reverse=True)
    return (l1+.05)/(l2+.05)

def on_color(accent):
    return max(('#FFFFFF','#111111'), key=lambda c: contrast(c,accent))

def render(recipe):
    p=recipe['palette']
    rows = [
        f'/* {recipe["name"]}: {recipe["style_mix"]}',
        '   Verify colors in actual interactive states. Do not overwrite existing brand tokens blindly. */',
        ':root {',
    ]
    for key,val in p.items():
        rows.append(f'  --ui-{key}: {val};')
    rows += [
        f'  --ui-on-accent: {on_color(p["accent"])};',
        '  --ui-font: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;',
        '  --ui-radius-sm: 0.5rem;',
        '  --ui-radius-md: 0.875rem;',
        '  --ui-radius-lg: 1.25rem;',
        '  --ui-space-1: 0.25rem;',
        '  --ui-space-2: 0.5rem;',
        '  --ui-space-3: 0.75rem;',
        '  --ui-space-4: 1rem;',
        '  --ui-space-6: 1.5rem;',
        '  --ui-space-8: 2rem;',
        '}',
        '',
        '@media (prefers-reduced-motion: reduce) {',
        '  *, *::before, *::after {',
        '    animation-duration: 0.01ms !important;',
        '    animation-iteration-count: 1 !important;',
        '    transition-duration: 0.01ms !important;',
        '    scroll-behavior: auto !important;',
        '  }',
        '}',
    ]
    return '\n'.join(rows)+'\n'

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--recipe', help='ID of recipe, e.g. quiet-enterprise')
    parser.add_argument('--list', action='store_true', help='List recipe IDs')
    parser.add_argument('--output', help='Optional file to write (no automatic project edits)')
    args=parser.parse_args()
    data=json.loads(CATALOG.read_text(encoding='utf-8'))['recipes']
    if args.list:
        for r in data: print(f'{r["id"]}: {r["name"]}')
        return
    if not args.recipe:
        parser.error('Specify --recipe or --list')
    item=next((r for r in data if r['id']==args.recipe),None)
    if not item:
        parser.error('Unknown recipe; use --list')
    css=render(item)
    if args.output:
        path=Path(args.output)
        if path.exists():
            parser.error(f'File already exists: {path} (refusing to overwrite)')
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(css,encoding='utf-8')
        print(f'Wrote {path}')
    else:
        print(css,end='')

if __name__=='__main__': main()
