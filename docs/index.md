---
hide:
  - toc
---

# TRON 2 Documentation

Practical, searchable documentation for the LimX Dynamics TRON 2, based on official manuals, public model repositories, and future Ubbink verification.

[Controller & VR](hardware/controller.md){ .md-button .md-button--primary }
[Start and stop](operation/startup.md){ .md-button }
[SDK development](software/index.md){ .md-button }

!!! warning "Documentation in review"

    This wiki summarizes source material; it does not replace the current official manual or approved safety instructions. Check the source and applicable robot configuration before acting.

<div class="tron-card-grid tron-card-grid--compact" markdown>

<div class="tron-card" markdown>
### [Operate](operation/index.md)
Startup, shutdown, emergency stop, handheld control, and VR teleoperation.
</div>

<div class="tron-card" markdown>
### [Understand the robot](hardware/robot-overview.md)
Configurations, interfaces, batteries, sensors, and status indications.
</div>

<div class="tron-card" markdown>
### [Develop](software/index.md)
SDK layers, supported environments, APIs, ROS integration, and robot models.
</div>

<div class="tron-card" markdown>
### [Diagnose](troubleshooting/index.md)
Safe first checks and the information to collect before escalation.
</div>

</div>

## Source status

| Source | Coverage | Wiki status |
| --- | --- | --- |
| TRON 2 User Manual, EDU edition, v0.1 | Hardware, operation, controller, VR, networking | Summarized; Ubbink verification pending |
| TRON 2 SDK Development Guide, v0.5 | Low/high-level APIs, software, upgrade references | Core structure imported |
| `limx-tron2/robot-description` | URDF, Xacro, MuJoCo, meshes, model variants | Repository structure documented |

See [Document sources](reference/document-sources.md) for versions, scope, and redistribution notes.
