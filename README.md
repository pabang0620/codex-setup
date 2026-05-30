# Codex Setup

Portable Codex/OMX agent setup copied from `/home/pabang/myapp`.

## Windows setup

```powershell
cd "$env:USERPROFILE\Desktop"
git clone https://github.com/pabang0620/codex-setup.git project
cd project
omx setup
codex -C .
```

## Notes

- Do not commit `auth.json`, `.env`, sqlite files, logs, or generated hook files.
- Run `omx setup` after cloning on a new machine so local hook paths are regenerated.
- Global YOLO mode still belongs in `$env:USERPROFILE\.codex\config.toml`.
