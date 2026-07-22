---
title: 1-1-robot-import-initial-scene-setup.md
---
# Vision-to-Pointing Development Roadmap



| Item | Value |
|------|-------|
| **Author** | Arjen van Dijk |
| **Date** | 22-07-2026 |
| **Operating System** | Ubuntu 24.04 |
| **Isaac Sim** | 6.0.1 |
| **Hardware** | NVIDIA GB10 Grace Blackwell Superchip |

---

## Objective

Import the correct TRON 2 robot model into Isaac Sim, verify that the USD loads correctly, create a clean baseline scene and save it for the remainder of the project.

---

## Robot Source

**Repository**

See: [Isaac Sim, Isaac Lab & FluxVLA Training → Robot model (URDF/USD)](../../software/isaac-sim-training.md#robot-model-urdfusd-for-isaac-sim) for the `limxdynamics/robot-description` repo.

**Robot Variant**

`DACH_TRON 2A`

**Dowloaded local USD File location**

`Home/Tron2/robot-description/tron2/DACH_TRON 2A/usd/robot.usd`

---

## Work Performed

The robot model was imported successfully into Isaac Sim without any missing USD references or asset errors.

The imported model already contained a correctly configured **Articulation Root**, so no modifications were required before enabling physics.

A Ground Plane was added using:

`Create → Physics → Ground Plane`

Two OmniPBR materials were created.

- One material was assigned to the robot. `(#2D1625)`
- One material was assigned to the Ground Plane. `(#000000)`

The robot material was applied to the top robot prim using **Stronger Than Descendants**, allowing the complete robot to receive the new colour.

The robot was initially positioned at:

```
X = 0
Y = 0
Z = 1.3
```

This allows the robot to settle (fall) naturally onto the Ground Plane when physics starts.

The complete scene was saved as the baseline project for all future experiments.

---

## Findings

The robot imported successfully without requiring modifications to the articulation.

The complete joint hierarchy is present inside the Stage Tree.

All joints and links appear to be correctly named.

No missing assets or import warnings were encountered.

The imported model is immediately usable for simulation.

---

## View

Renderer: RTX Real-Time 2.0

Approximate Performance: ~40 FPS

Light: Grey Studio


---

## Figure



---

## Next Step

Continue with **Phase 1.2 – Robot Inspection & Reference Scene**.
