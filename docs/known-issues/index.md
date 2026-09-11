# Known Issues

Short, standalone pages for specific bugs and fixes found during TRON 2 development — pulled out of the dated build logs so they're searchable on their own, without reading the whole session.

Each page follows the same shape: **Symptom → Cause → Fix**, plus a link back to the build-log session it came from.

| Issue | Area | Source log |
| --- | --- | --- |
| [bf16 crash on GB10 (JAX / Blackwell)](jax-bf16-gb10.md) | DGX Spark, JAX/OpenPI | Aug 28 |
| [FluxVLA vs tron2_openpi checkpoints aren't compatible](checkpoint-format-mismatch.md) | Deployment | Aug 28 |
| [rospy.init_node() ordering breaks the Bridge](ros-bridge-init-order.md) | ROS bridge | Aug 28 |

More to come — the Aug 25/26 install and tokenizer logs have several more worth extracting (protobuf version conflict, tokenizer `vocab_size=5` bug, LeRobot v3 vs v2.1, DGX UEFI boot order, compliance switch/preset independence). Ask to have the next batch drafted.
