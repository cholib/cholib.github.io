import re
from glob import glob

paths = glob('_featured_categories/*.md') + glob('_featured_tags/**/*.md', recursive=True)
all_nodes = []
for p in paths:
    txt = open(p, encoding='utf-8').read()
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', txt, re.S)
    if not m:
        continue
    fm = {}
    for line in m.group(1).splitlines():
        if ':' not in line:
            continue
        k, v = line.split(':', 1)
        fm[k.strip()] = v.strip().strip('"\'')
    if fm.get('sidebar') in ('true', 'True', 'yes', 'Yes'):
        fm['_path'] = p
        all_nodes.append(fm)

print('SIDEBAR TRUE NODES:', len(all_nodes))
for n in sorted(all_nodes, key=lambda x: (x.get('type',''), int(x.get('order','0')) if x.get('order','0').isdigit() else 0, x.get('title',''))):
    print(n.get('type'), n.get('title'), n.get('category'), n.get('slug'), n.get('_path'))

cats = [n for n in all_nodes if n.get('type') != 'tag']
print('\nTOP LEVEL NODES:')
for n in cats:
    subs = [m for m in all_nodes if m.get('type') == 'tag' and m.get('category') == n.get('slug')]
    print(n.get('title'), n.get('slug'), '->', len(subs), [s.get('title') for s in subs])
