# Policy management

Policies are selected from locally maintained folders. This wiki describes their contract and validation, not a downloadable launcher implementation.

## What a policy folder identifies

| Item | Purpose |
| --- | --- |
| Policy name | Identifies the selected model in both logs and readiness metadata |
| `policy.yaml` | Task text and model/server configuration |
| Weights/configuration | LeRobot pretrained model or an OpenPI checkpoint |
| Saved train/test split | Recommended provenance for an own-trained model |
| Model-specific start pose | A valid recorded start state and its motion settings |

The measured own-model workflow uses `~/tron2-policies/<name>/`. The local `zet-policy-neer` utility takes task text from the dataset and validates the folder. `start-server` lists policies, can select one directly, or only list them.

A correctly packaged policy should be an additional folder/configuration, not a code change.

## Two shortcuts

| Shortcut | Model family | Current status |
| --- | --- | --- |
| TRON2 policy-server (eigen) | Own ACT/SmolVLA, LeRobot/PyTorch | Command path and real execution tested; physical desktop click not recorded as tested |
| TRON2 policy-server (LimX) | LimX OpenPI/JAX checkpoints | **Built, untested**, owner update 2 October 2026 |

Both use the shared safety client. Do not run the two servers together or alongside a training: JAX's memory reservation can consume most of the GPU budget.

## Fail early

The tested own-model launcher refuses missing weights, missing task text, incompatible camera count, an unavailable OpenPI dependency and an unknown configuration. A wrong policy already bound to the port must not pass readiness.

The LimX implementation has changed since the source document described it as merely specified. Keep its hardware-test status separate from that implementation status.

**Source:** [UBB-CLIENT-001](../reference/document-sources.md), section 16.6; [UBB-POL-001](../reference/document-sources.md), sections 17.1–17.2 and 17.6; owner clarification 2 October.
