#!/usr/bin/env python3
from pathlib import Path
import tomllib

bad = []
for path in sorted(Path(".codex/agents").glob("*.toml")):
  try:
    tomllib.loads(path.read_text(encoding="utf-8"))
  except Exception as exc:
    bad.append((path.name, str(exc)))

print(f"bad {len(bad)}")
for name, error in bad:
  print(name, error)
