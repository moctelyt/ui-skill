#!/usr/bin/env python3
"""Validate catalog structure, recipe IDs and base foreground contrast."""
import json
import re
import sys
from pathlib import Path
from theme_tokens import contrast, on_color

BASE=Path(__file__).resolve().parents[1]/'references'
HEX=re.compile(r'^#[0-9a-fA-F]{6}$')

def main():
    catalog=json.loads((BASE/'style-catalog.json').read_text(encoding='utf8'))
    recipes=json.loads((BASE/'theme-recipes.json').read_text(encoding='utf8'))
    errors=[]
    styles=catalog['styles']
    if len(styles)!=220 or catalog['total']!=len(styles): errors.append('Style catalog must contain exactly 220 entries')
    if len({x['slug'] for x in styles})!=len(styles): errors.append('Duplicate style slugs')
    if [s['id'] for s in styles]!=list(range(1,len(styles)+1)): errors.append('Style IDs not consecutive')
    if recipes['total']!=len(recipes['recipes']): errors.append('Recipe count mismatch')
    if len({r['id'] for r in recipes['recipes']})!=len(recipes['recipes']): errors.append('Duplicate recipe IDs')
    for r in recipes['recipes']:
        palette=r['palette']
        for name in ('bg','surface','text','muted','accent','border'):
            if not HEX.fullmatch(palette.get(name,'')): errors.append(f'{r["id"]}: invalid palette.{name}')
        if not all(HEX.fullmatch(x) for x in palette.values()): continue
        for key in ('bg','surface'):
            for foreground in ('text','muted'):
                ratio=contrast(palette[foreground],palette[key])
                if ratio<4.5:
                    errors.append(f'{r["id"]}: {foreground} on {key} contrast {ratio:.2f}:1 below 4.5:1')
        if contrast(on_color(palette['accent']),palette['accent'])<4.5:
            errors.append(f'{r["id"]}: accent cannot support AA normal text with black/white')
    if errors:
        for err in errors: print('ERROR:',err,file=sys.stderr)
        return 1
    print(f'OK: {len(styles)} catalog entries, {len(recipes["recipes"])} recipes; base text/surface contrast >= 4.5:1, readable on-accent tokens.')
    print('Note: border, focus, disabled, charts, overlays, glass/gradient and real component states require separate testing.')
    return 0

if __name__=='__main__': sys.exit(main())
