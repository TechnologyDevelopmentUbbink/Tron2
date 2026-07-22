# TRON 2 Documentation

This repository contains the static MkDocs Material documentation website and internal knowledge-base foundation for the LimX Dynamics TRON 2 robot.

https://technologydevelopmentubbink.github.io/Tron2/

## Repository structure

- `docs/` contains all content published by MkDocs, including Markdown pages and website assets.
- `mkdocs.yml` controls the theme, extensions, and navigation.
- `source-documents/` is a working area for original manuals and other source material; it is not published automatically.
- `site/` is generated build output and is ignored by Git.

## Install and preview

```powershell
python -m pip install mkdocs mkdocs-material
python -m mkdocs serve
```

Open `http://127.0.0.1:8000` while the preview server is running. Stop it with ++ctrl+c++.

Validate the complete site before opening a pull request:

```powershell
python -m mkdocs build --strict
```

## Contributing

Create or edit Markdown files under `docs/`, register new pages in `mkdocs.yml`, preview locally, and submit changes through a branch and pull request. The website's Edit action opens the corresponding Markdown file in GitHub.

Review the [contributing documentation](https://technologydevelopmentubbink.github.io/Tron2/contributing/) for writing, classification, image, and review guidance.

## Versioning

The site currently publishes one documentation stream from `main`; multi-version publishing is not enabled. Robot firmware, SDK, package, and hardware compatibility is tracked separately in the documentation. See `docs/contributing/versioning.md` for the proposed versioning approach.

## Source-document handling

Before committing manuals or working material, check confidentiality, copyright, and redistribution restrictions. Never add credentials, tokens, internal addresses, or sensitive Ubbink information.

The repository is hosted at [TechnologyDevelopmentUbbink/Tron2](https://github.com/TechnologyDevelopmentUbbink/Tron2). MkDocs generates a static website: it has no database, backend, or login system.
