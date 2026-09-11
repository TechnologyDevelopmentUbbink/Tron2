---
hide:
  - toc
---

# TRON 2 knowledge base

Practical, searchable documentation for the LimX Dynamics TRON 2 — based on official manuals, public model repositories, and hands-on Ubbink verification.

<div class="tron-doors" markdown>

<div class="tron-door" markdown>
### [Hardware Specs](getting-started/index.md)

The manual. Robot, controller, VR, batteries, sensors, startup/shutdown, e‑stop.

**[Start here to set up or operate something →](getting-started/index.md)**
</div>

<div class="tron-door" markdown>
### [Software Dev](software/index.md)

SDK, ROS, Isaac Sim, FluxVLA training and deployment — plus our own discoveries.

**[Start here to build or debug something →](software/index.md)**
</div>

</div>

<div class="tron-issues" markdown>
### Known issues — quick lookup

[bf16 crash on GB10 (JAX / Blackwell)](known-issues/jax-bf16-gb10.md)
[FluxVLA vs tron2_openpi checkpoints aren't compatible](known-issues/checkpoint-format-mismatch.md)
[rospy.init_node() ordering breaks the Bridge](known-issues/ros-bridge-init-order.md)

**[See all known issues →](known-issues/index.md)**
</div>

<div class="tron-card-grid tron-card-grid--compact" markdown>

<div class="tron-card" markdown>
### [Operate](operation/index.md)
Startup, shutdown, emergency stop, handheld control, and VR teleoperation.
</div>

<div class="tron-card" markdown>
### [Diagnose](troubleshooting/index.md)
Safe first checks and the information to collect before escalation.
</div>

<div class="tron-card" markdown>
### [Reference](reference/specifications.md)
Specifications, system architecture, terminology, and command reference.
</div>

<div class="tron-card" markdown>
### [Contribute](contributing/index.md)
How to edit pages, add images, and get changes reviewed.
</div>

</div>

## Source status

| Source | Coverage | Wiki status |
| --- | --- | --- |
| TRON 2 User Manual, EDU edition, v0.1 | Hardware, operation, controller, VR, networking | Summarized; Ubbink verification pending |
| TRON 2 SDK Development Guide, v0.5 | Low/high-level APIs, software, upgrade references | Core structure imported |
| `limx-tron2/robot-description` | URDF, Xacro, MuJoCo, meshes, model variants | Repository structure documented |

See [Document sources](reference/document-sources.md) for versions, scope, and redistribution notes.
