---
hide:
  - toc
---

# TRON 2 knowledge base

Practical, searchable documentation for the LimX Dynamics TRON 2 — based on official manuals, public model repositories, and hands-on Ubbink verification.

!!! warning "Documentation in review"

    This wiki summarizes source material; it does not replace the current official manual or approved safety instructions. Check the source and applicable robot configuration before acting.

<div class="tron-doors" markdown>

<a class="tron-door" href="getting-started/index.md" markdown>
<span class="tron-door__title">Hardware Specs</span>
<p class="tron-door__desc">The manual. Robot, controller, VR, batteries, sensors, startup/shutdown, e‑stop.</p>
<span class="tron-door__cta">Start here to set up or operate something →</span>
</a>

<a class="tron-door" href="software/index.md" markdown>
<span class="tron-door__title">Software Dev</span>
<p class="tron-door__desc">SDK, ROS, Isaac Sim, FluxVLA training and deployment — plus our own discoveries.</p>
<span class="tron-door__cta">Start here to build or debug something →</span>
</a>

</div>

<div class="tron-issues" markdown>
<p class="tron-issues__title">Known issues — quick lookup</p>

[bf16 crash on GB10 (JAX / Blackwell)](known-issues/jax-bf16-gb10.md)
[FluxVLA vs tron2_openpi checkpoints aren't compatible](known-issues/checkpoint-format-mismatch.md)
[rospy.init_node() ordering breaks the Bridge](known-issues/ros-bridge-init-order.md)

<p class="tron-issues__more"><a href="known-issues/index.md">See all known issues →</a></p>
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
