# TRON 2 Documentation

Static MkDocs Material site and internal knowledge base for the LimX Dynamics TRON 2 robot.

**Live site:** https://technologydevelopmentubbink.github.io/Tron2/

## Repository structure

- `docs/` — all published content: Markdown pages and site assets.
- `mkdocs.yml` — theme, extensions, and navigation.
- `source-documents/` — original manuals and source material; not published automatically.
- `site/` — generated build output, gitignored.

## Preview locally

```powershell
python -m pip install mkdocs mkdocs-material
python -m mkdocs serve
```

Open `http://127.0.0.1:8000`. Stop with ++ctrl+c++.

Before pushing, validate the build:

```powershell
python -m mkdocs build --strict
```

See [Contributing](docs/contributing/index.md) for how to add or edit pages.
