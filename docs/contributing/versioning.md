# Documentation Versioning :D

This page explains the difference between website versions, robot/software compatibility, and ordinary page revisions.

!!! info "Current state: one development stream"

    Multi-version website publishing is not enabled. The current site is built from the repository's `main` branch and should be treated as developing documentation until a release policy is approved.

## Three kinds of version information

| Kind | Purpose | Current location |
| --- | --- | --- |
| Documentation website version | Preserves separate published editions of the complete site | Not enabled |
| Robot and software compatibility | Records which hardware, firmware, SDK, ROS package, or tool combinations apply | [Version compatibility](../software/version-compatibility.md) |
| Documentation revision | Records important content and source changes | [Revision history](../reference/revision-history.md) and Git history |

## What is already available

- Git records every committed documentation change.
- Pages can state applicable firmware, SDK, package, and hardware versions.
- The compatibility page is ready for a verified version matrix.
- The revision-history page is ready for meaningful documentation releases.

These features support traceability, but they do not provide a version selector or archived copies of the full website.

## Proposed published-version approach

Material for MkDocs commonly uses a separate version-management tool such as Mike for version selectors and archived site builds. Mike is not currently installed or configured for this repository.

Before enabling multi-version publishing, decide:

1. Whether users need to view older documentation editions.
2. What creates a new documentation version.
3. How versions relate to robot hardware and software releases.
4. Which version is shown as latest.
5. How unsupported or obsolete versions are labelled.
6. Where versioned static builds will be hosted.

!!! warning "Do not enable a selector without archived builds"

    A version selector is useful only when the corresponding documentation editions are actually built and published. Adding the visual control alone would create broken links.

## Suggested release labels

- `dev` for the changing development documentation
- A numbered documentation release for reviewed snapshots
- `latest` as an alias to the currently supported release

The exact numbering convention is not yet decided. Do not infer it from robot firmware or SDK versions unless the release policy explicitly couples them.

## Until versioned publishing is enabled

- Mark content **Version dependent** where appropriate.
- Record all applicable versions with procedures and mappings.
- Keep compatibility tables evidence-based.
- Use Git history and the revision-history page for traceability.
- Treat the Edit button as targeting the current `main` source, not an archived documentation edition.
