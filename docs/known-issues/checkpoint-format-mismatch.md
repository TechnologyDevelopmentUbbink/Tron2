---
tags:
  - FluxVLA
  - Deployment
  - Checkpoints
---

# FluxVLA vs tron2_openpi checkpoints aren't compatible

**Symptom**

A checkpoint trained with FluxVLA fails (or silently loads wrong) when passed to `tron2_openpi`'s `PI0Pytorch.load_pytorch` / `safetensors.torch.load_model`.

**Cause**

FluxVLA and `tron2_openpi` are two independently-implemented "dialects" of the same pi0.5 architecture, built by different teams at LimX. Parameter key names don't match between them:

| FluxVLA checkpoint | `tron2_openpi` (`PI0Pytorch`) |
| --- | --- |
| `llm_backbone.embed_tokens.weight` | `paligemma_with_expert...` |
| `action_in_proj.projector.weight` | `action_in_proj.weight` (no `.projector.`) |

`tron2_openpi` is a fork of Physical Intelligence's original OpenPI; FluxVLA is LimX's own broader training platform. Neither shares checkpoint-layer naming with the other — confirmed by the fact that LimX's own published candy/cloth/banana/sort checkpoints are *not* trained with FluxVLA either, they ship separately in OpenPI's native format.

**Fix**

Don't try to load a FluxVLA checkpoint into `tron2_openpi`. Use FluxVLA's own native TRON2 deployment path instead: `Tron2InferenceRunner` (`fluxvla/engines/runners/tron2_inference_runner.py`), which talks to the robot over ROS1 rather than the OpenPI WebSocket client/server pattern. See LimX's own tutorial: `fluxvla.limxdynamics.com/zh/md_source/tutorials/inference/Tron2.html`.

A key-mapping conversion script between the two formats is possible but carries real risk of silent errors — not attempted, since the native path exists and works.

**Related**

- Source: build log, Aug 28 (not yet migrated into the wiki as its own page)
