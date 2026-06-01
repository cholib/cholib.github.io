import os
import re
from pathlib import Path

root = Path(r"d:\cholib\cholib.github.io")
posts = []
for p in root.rglob("_posts/**/*.md"):
    with p.open("r", encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"---\s*\n(.*?\n)---\s*\n", text, re.S)
    if not m:
        continue
    fm = m.group(1)
    data = {}
    for line in fm.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip()
    posts.append((p.relative_to(root), data.get("title", ""), data.get("category", ""), data.get("tags", "")))
for p, title, category, tags in sorted(posts):
    print(f"{p} | category={category} | tags={tags} | title={title}")
print(f"Total posts: {len(posts)}")
