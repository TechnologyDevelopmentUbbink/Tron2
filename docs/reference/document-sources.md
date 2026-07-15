# Document sources

This register records provenance, version, permitted use, and known gaps.

| ID | Source | Version/date | Classification | Used for | Notes |
| --- | --- | --- | --- | --- | --- |
| LIMX-UM-001 | [TRON 2 User Manual](https://limx.cn/en/documents/852949782845591552) | TRON 2 EDU, v0.1; page dated 11 June 2026 | Official source | Hardware, controller, VR, operation, networking | Supplied PDF contains a redistribution restriction; PDF and screenshots are not committed |
| LIMX-SDK-001 | [TRON 2 SDK Development Guide](https://limx.cn/en/documents/856848486581276672) | Supplied PDF v0.5; revision 13 January 2026; cover 20260225 | Official source | SDK architecture and APIs | Contains default credentials/private addresses; those are omitted |
| LIMX-RD-001 | [limx-tron2/robot-description](https://github.com/limx-tron2/robot-description) | Pin not yet recorded | Official public repository | Variants, URDF/Xacro, MuJoCo, meshes, sensor/model notes | Apache-2.0; match variant before use |

## Import rules

- Summarize and paraphrase; do not reproduce manuals or screenshots without redistribution permission.
- Cite document title, revision, and section/page where practical.
- Never publish credentials, serial numbers, account details, internal addresses, or sensitive Ubbink screenshots.
- Separate official claims from Ubbink verification.
- Record firmware, SDK, ROS, hardware revision, and repository commit when behavior is version dependent.

## Local source files

Original manuals may be kept under the local `source-documents/` workflow only after confidentiality and redistribution checks. MkDocs does not publish that folder, but Git can still publish committed files—therefore the supplied PDFs have not been copied into the repository.
