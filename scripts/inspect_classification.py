from pathlib import Path
root = Path(r"d:\cholib\cholib.github.io")
for p in root.rglob('*.md'):
    if '.git' in p.parts:
        continue
    text = p.read_text(encoding='utf-8', errors='ignore')
    if not text.startswith('---'):
        continue
    parts = text.split('---', 2)
    if len(parts) < 3:
        continue
    fm = parts[1]
    data = {}
    for line in fm.splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            data[k.strip()] = v.strip()
    if 'category' in data or 'categories' in data or 'tags' in data:
        print(p.relative_to(root), data)
