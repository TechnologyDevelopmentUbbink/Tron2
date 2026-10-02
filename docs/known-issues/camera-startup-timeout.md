# All cameras hit first_frame_timeout

**Status: root cause unresolved.** The 1 October record reports first-frame timeouts on all three live cameras.

The controller answered, but without images the client could not assemble a complete observation. Fault handling attempted rest; when arrival failed, the client held instead of exiting.

This establishes the recovery behaviour, not a camera fix. Record Bridge connection/service state, subscribed image names, first-frame timing and state availability when investigating. Check the [known Bridge prerequisites](ros-bridge-init-order.md), but do not declare init ordering the cause without evidence.

[Observation paths](../reference/observation-pipeline.md) · [Physical session](../projects/experiments/2026-10-01-robot-session.md) · [Manual recovery](../deployment/run-a-policy.md#if-the-rest-route-fails).

**Source:** UBB-POL-001 sections 17.7–17.8, [source register](../reference/document-sources.md).
