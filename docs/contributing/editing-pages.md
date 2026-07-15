# Editing Pages

Documentation pages are Markdown files under `docs/`. The site navigation and page order are controlled by `mkdocs.yml` in the repository root.

## Preview locally

From the repository root, install the required packages and start the preview:

```powershell
python -m pip install mkdocs mkdocs-material
python -m mkdocs serve
```

Open `http://127.0.0.1:8000`. The server reloads when saved files change.

## Create a page

1. Choose the appropriate section under `docs/`.
2. Create a lowercase, hyphen-separated `.md` filename.
3. Add one level-one title and a short introduction.
4. Mark incomplete or unverified technical content clearly.
5. Add the file to the matching section in `mkdocs.yml`.
6. Preview it and run `python -m mkdocs build --strict`.

## Navigation and links

Indent YAML carefully when adding a page to `nav`. Use relative Markdown links between pages and verify every link in the local preview.

## GitHub Edit button

The Edit action opens the current page's Markdown source through `edit/main/docs/` on GitHub. It is a source-file link, not an editor embedded in the website.

!!! info "Why Edit can return 404 during local preview"

    A local preview can contain files that do not yet exist on GitHub. The Edit button always opens the configured GitHub `main` branch, so GitHub returns 404 until that Markdown file has been committed and pushed to that branch. It can also return 404 when the branch name is different or the viewer does not have access to a private repository.

The expected workflow is:

1. Edit the local Markdown file directly while previewing.
2. Commit the page to a branch when authorized.
3. Push the branch and open a pull request.
4. After the file exists on GitHub, use the Edit action for future changes.

GitHub permissions and the normal review workflow still apply. Do not change `edit_uri` merely to hide a local-preview 404.

## Branch and pull request workflow

1. Update the local `main` branch according to the team's Git workflow.
2. Create a short-lived branch with a descriptive name.
3. Make and validate focused documentation changes.
4. Commit with a clear message and push the branch when authorized.
5. Open a pull request, describe the evidence and classifications used, and request technical review.

Do not include confidential material, credentials, or restricted source documents.
