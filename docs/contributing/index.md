# Contributing

Write for someone trying to complete a task or avoid a previously observed failure.

## Keep pages useful

Give each page one purpose, a short introduction and clear links to related topics. Procedures explain prerequisites, steps, expected results and relevant failure handling. Technical reference pages define the exact contract.

Store dated measurements and failed attempts under Projects / Experiments. Link to that evidence from the current topic; do not duplicate a long session report throughout the wiki. Preserve important old URLs with a short relocation page when moving content.

Remove empty headings, repeated filler and conversational to-do messages. Keep unknown facts explicitly unknown. Use English prose while retaining actual Dutch local command names/messages with translations.

Operational code changes frequently and is not distributed here. Document stable concepts and recurring pitfalls; do not create broken links or imply that local utilities can be installed from this repo.

## Evidence labels

| Label | Meaning |
| --- | --- |
| Official source | Vendor claim, with revision/section |
| Ubbink measured | Observed in the stated robot session or environment |
| Mock tested | Tested against the described rig; not equivalent to physical verification |
| Practical observation | Seen in use, without complete validation |
| Built, untested | Implementation exists; operation not established |
| Unverified / unresolved | Unknown or open investigation |
| Version dependent | Record the tested version/date and scope |

A single success does not verify an entire subsystem. Do not mark hardware, firmware or controller tables fully tested because one policy session worked.

## Publishing

Add the page to mkdocs.yml navigation and check every local link. Install the pinned documentation requirements, preview with python -m mkdocs serve, then run python -m mkdocs build --strict. Inspect landing pages in light/dark mode and at phone width.

Changes may be committed to main after validation. Keep credentials, internal addresses, restricted manuals and private operational code out of commits. The source register explains provenance and source-file handling.
