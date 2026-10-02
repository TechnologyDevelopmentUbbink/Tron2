# Known issues

Look up a symptom here; use [First triage](../troubleshooting/index.md) when the category is unclear.

| Issue | Context | Evidence / status |
| --- | --- | --- |
| [JAX bf16 on GB10](jax-bf16-gb10.md) | OpenPI compilation | August workaround; upstream status is a dated snapshot |
| [Checkpoint formats](checkpoint-format-mismatch.md) | FluxVLA vs OpenPI | Parameter naming/runtime mismatch; August investigation |
| [Bridge init order](ros-bridge-init-order.md) | ROS1/Bridge integration | Ordering, URL scheme and joint-topic alignment |
| [LeRobot environment](lerobot-environment.md) | ARM packages and decoders | Working environment measured September |
| [Recording/statistics](dataset-recording.md) | Dataset quality | Clean-copy mitigation; recorder cause unresolved |
| [Viewer/cameras](viewer-and-cameras.md) | Rerun and model input | Connection and mapping fixes |
| [movej without motion](movej-no-motion.md) | Active developer mode | Physical route used servoj instead |
| [Camera first-frame timeout](camera-startup-timeout.md) | Live observation startup | Recovery observed; root cause unresolved |

Use the current topic pages for procedures. A historical workaround is not proof that an upstream issue remains open today.
