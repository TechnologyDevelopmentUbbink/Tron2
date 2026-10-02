# LeRobot environment pitfalls

**Symptoms:** installation fails on aarch64, video decoding silently changes backend, or an offline SmolVLA fine-tune reports migration errors.

| Cause in the tested setup | Resolution |
| --- | --- |
| Python/dependency conflicts in the Isaac Lab image | Use the separate host environment |
| TorchCodec release lacks a matching ARM wheel | Use the measured torch 2.11 / TorchCodec 0.11 combination |
| Missing FFmpeg libraries | Validate the system libraries and known-frame decoder check |
| Silent PyAV fallback | Explicit backend selection and installation verification |
| Missing first-use processor/base-model files | Populate the cache while connected before offline use |
| WebSocket packages confused | Distinguish websocket-client, websockets and msgpack |
| uv environment has no pip | Use its environment-aware package tooling |

[Working versions](../learning/lerobot-setup.md) · [Measured evidence](../projects/experiments/2026-09-30-deployment.md).

**Source:** UBB-IL-001 sections 3, 8.8, 14.4 and 15.6, [source register](../reference/document-sources.md). These are version-specific findings.
