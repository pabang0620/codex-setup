#!/usr/bin/env python3
from pathlib import Path

bad = []
for path in sorted(Path(".agents/skills").glob("*/SKILL.md")):
  if not path.read_text(encoding="utf-8").startswith("---\n"):
    bad.append(str(path))

print(f"bad {len(bad)}")
for path in bad:
  print(path)
