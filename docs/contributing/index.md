# Contributing

How to add or edit pages in this wiki, and the status labels used throughout it.

## Adding a page

1. Create a lowercase, hyphen-separated `.md` file under `docs/`.
2. Give it one `# Title` and a short intro.
3. Add it to `mkdocs.yml`'s `nav:` section.
4. Preview locally: `python -m mkdocs serve`, open `http://127.0.0.1:8000`.
5. Before pushing: `python -m mkdocs build --strict` should pass with no warnings.

Commit straight to `main` — open a PR only if you want a second pair of eyes on something. Just never commit credentials, passwords, or restricted source material.

## Status labels

Mark technical content with how solid it is. You're already doing this in session logs (`Status: hands-on verified`) — the same idea applies to wiki pages:

| Label | Meaning |
| --- | --- |
| **Official source** | Straight from LimX Dynamics docs. Note the document + version. |
| **Ubbink verified** | Tested on our own TRON 2. |
| **Practical observation** | Seen in use, not yet formally checked. |
| **Unverified** | Uncertain, translated, or untested — don't rely on it for safety-critical steps. |
| **Version dependent** | Behavior may change by firmware/SDK/ROS version — say which version you tested. |

When in doubt, pick the weaker label. Stale or wrong content is worse than an honest "unverified".
