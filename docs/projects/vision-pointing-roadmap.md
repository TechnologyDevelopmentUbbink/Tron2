---
title: Vision-to-Pointing Development Roadmap
---

# Vision-to-Pointing Development Roadmap

Source status: internal project plan, partly Unverified until each phase is executed. Not yet Ubbink-verified end to end.

This page is a **living build log**, not a fixed spec. Each checklist item gets updated in place as work happens: software/version used, what worked, what didn't, dead ends. If the project stalls at any phase, this page should still stand on its own as a usable record for whoever picks it up next (including future-you).

Primary first use case: place a coloured cube in front of the robot and make one arm point toward it without touching it.

Superseded document

This page replaces the original Word roadmap (`Vision-to-Pointing Development Roadmap.docx`, kept in `source-documents/` for archive only). Do not edit the Word file going forward — this page is the live version.

## How the complete system will eventually work

The final system is not one giant AI model. It is a chain of small modules, each receiving a defined data type and sending a defined data type to the next module:

```
Camera frame (RGB+D) → Target selection → 3D position (camera frame)
  → Coordinate transform (→ robot base) → Pointing pose → IK/motion planner
  → TRON 2 SDK robot command
```

### Official SDK facts used in this guide

- The TRON 2 SDK distinguishes simulation at `127.0.0.1` from the real robot at `10.192.1.2`.
- The SDK exposes robot state: joint angle `q`, velocity `dq`, estimated torque `tau`.
- The low-level example publishes position, velocity, torque, `Kp`, `Kd` commands at 300 Hz — safety-critical, treat as last resort.
- The EDU compute module is intended for robot-related algorithms and can talk to the robot controller over the robot network.

Version dependent

Exact availability/naming of high-level Cartesian or ServoJ functions must be checked against the installed firmware and SDK version before implementation.

### Robot model for Isaac Sim

Don't re-solve this here — see [Isaac Sim, Isaac Lab & FluxVLA Training → Robot model (URDF/USD)](../software/isaac-sim-training.md#robot-model-urdfusd-for-isaac-sim) for the `limxdynamics/robot-description` repo and import steps. Phase 1 Task 1 below just points back to that.

---

## Project rule

Each phase must produce saved evidence before the next phase starts. This keeps vision, calibration, motion planning, SDK communication, and (later) VLM behaviour from all failing at once and being impossible to untangle.

| Phase | Summary |
|---|---|
| 1. Simulation | Simulated cube → simulated TRON 2 points at it |
| 2. Real control | Same motion, on the real TRON 2, target still manual |
| 3. Camera | Real RGB-D camera → measured 3D target |
| 4. VLM | Natural-language object selection, geometry stays deterministic |

---

## PHASE 1 — Simulated cube → simulated TRON 2 points at it

**Goal:** learn Isaac Sim and prove the geometry + arm-motion chain before any camera or physical robot is involved.

**Data contract:** input = exact cube position from the Isaac stage. Output = simulated joint targets and a visible pointing pose. No camera, no VLM, no real robot.

**Definition of "pointing":** use one clearly named pointing frame (e.g. right gripper centre, or a temporary `pointer_tip` frame). The target pose stops *before* the cube, doesn't collide with it:

```
pointer_position = cube_position - safety_offset × pointing_direction
```

### Checklist

#### 1.1 — Get a writable Isaac Sim project with the TRON 2 model loaded

- [ ] Clone `limxdynamics/robot-description`, pick the TRON 2 variant matching your hardware (dual-arm/desktop). See linked page above for exact steps.
- [ ] If no ready `.usd`: import via Isaac Sim's URDF Importer extension.
- [ ] Saved `.usd`/`.usda` scene opens without missing references.
- [ ] Robot appears with expected links and joints; **Articulation Root** is set correctly (per the linked page, this is the most common source of silent physics failures — check it explicitly, don't assume).

<details><summary>Build log</summary>

Unverified — not yet attempted at time of writing.

- Software/version:
- Worked:
- Didn't work / gotchas:

</details>

#### 1.2 — Confirm joint mapping

- [ ] Joint mapping note saved (which URDF joint name = which physical joint, arm side, DOF order).
- [ ] Cube can be moved numerically in the stage (script or console — not just dragging in viewport).
- [ ] Named end-effector or pointer frame recorded (decide now: gripper centre vs. dedicated `pointer_tip` frame, and write down why).

<details><summary>Build log</summary>

Unverified.

- Software/version:
- Worked:
- Didn't work / gotchas:

</details>

#### 1.3 — Read cube pose and print it (no motion yet)

- [ ] First program only reads the cube pose and prints `[x,y,z]` — resist the urge to wire up motion before this is solid.
- [ ] Printed values match the viewport (move the cube, confirm the printed numbers track it).

<details><summary>Build log</summary>

Unverified.

- Software/version:
- Worked:
- Didn't work / gotchas:

</details>

#### 1.4 — World-to-base transform

- [ ] World-to-base transform test passes (cube's world-frame pose converts correctly to robot base frame — this is the same transform machinery Phase 3 will reuse for real camera data, so get it right here).

<details><summary>Build log</summary>

Unverified.

- Software/version:
- Worked:
- Didn't work / gotchas:

</details>

#### 1.5 — Generate the pointing pose

- [ ] Pose marker appears in front of cube using `pointer_position = cube_position - safety_offset × pointing_direction`.
- [ ] `safety_offset` value decided and recorded (start conservative, e.g. 20–30 cm per the original data contract note).

<details><summary>Build log</summary>

Unverified.

- Software/version:
- Worked:
- Didn't work / gotchas:

</details>

#### 1.6 — IK / motion generation

- [ ] IK solver chosen and recorded here (Lula IK vs. cuRobo — check what LimX's own Isaac Lab repos use as a default before picking, since matching their convention may save integration pain later).
- [ ] Joint targets stay inside limits.
- [ ] Arm points without self-collision or cube contact.

<details><summary>Build log</summary>

Unverified.

- Software/version:
- Worked:
- Didn't work / gotchas:

</details>

#### 1.7 — Phase 1 exit gate

- [ ] Moving the cube to **5 different reachable positions** causes the simulated arm to point correctly and repeatably.
- [ ] Short video saved.
- [ ] All 5 target coordinates saved alongside the video.

Do not start Phase 2 until this gate passes.

---

## PHASE 2 — First real-robot test (target still manual)

**Goal:** make the physical TRON 2 reproduce a deliberately small, safe pointing motion. Target is still manually supplied — vision is not added yet.

**Preferred control path:** use a high-level Cartesian, ServoJ, or end-pose interface when LimX provides one. Only drop to low-level 300 Hz joint commands after the high-level route has been evaluated and its safety behaviour understood.

### Checklist

- [ ] Read-only SDK connection succeeds (ping, motor count, `q`/`dq`/`tau` stream printed — **no motion**).
- [ ] Emergency-stop procedure written down and rehearsed before anything moves.
- [ ] High-level arm interface tested.
- [ ] Sim-to-real joint map completed (does Isaac's joint order/naming match the SDK's?).
- [ ] Safety checklist signed off.
- [ ] Small commanded pose change succeeds.
- [ ] Target point recorded in robot-base coordinates; calculated pose logged *before* execution, not just after.
- [ ] Robot moves smoothly while state is logged.
- [ ] Error report saved (even/especially if there were no errors — note that).
- [ ] **Exit gate:** physical robot points toward 3 manually specified targets while staying inside a deliberately restricted workspace. Repeatable, observable, stoppable.

<details><summary>Build log</summary>

Unverified — Phase 1 not yet complete.

</details>

*(This phase will get the same item-by-item depth as Phase 1 once you're actually working through it.)*

---

## PHASE 3 — Real RGB-D camera → measured 3D target

**Goal:** replace the manually entered target with a measured one. After the target reaches robot-base coordinates, the rest of the chain is identical to Phase 2.

**The key idea:** don't "put the real block into Isaac" as the control method. Convert the detected block into a robot-base-frame coordinate — the transform, not a visual copy, is what makes the arm move correctly. Isaac may show the point as a marker/digital twin for validation only.

### Pipeline

```
RGB image → Depth image → Camera intrinsics (fx,fy,cx,cy) → 3D point (camera frame)
  → Extrinsic transform (camera→base) → Phase 2 motion chain
```

### Checklist

- [ ] Camera hardware decided and recorded here (RealSense vs. TRON 2 onboard RGB-D).
- [ ] One synchronized RGB+depth frame saved.
- [ ] `fx, fy, cx, cy` and depth scale recorded.
- [ ] Cube detection: mask, bounding box, centre pixel `(u,v)` — start with HSV thresholding.
- [ ] Depth read at centre/median over mask; missing/zero/noisy depth rejected.
- [ ] Camera-frame point `[Xc,Yc,Zc]` printed in metres, stable across frames.
- [ ] `T_base_camera` calibration done (hand-eye calibration — budget real time for this, it's usually the long pole of this whole phase) and saved with version/date.
- [ ] Base-frame `[Xb,Yb,Zb]` printed.
- [ ] Marker in Isaac/RViz follows the real cube when moved.
- [ ] Accuracy table completed across 5 positions; outliers explained, not hand-waved.
- [ ] Unsafe/low-confidence targets rejected before motion.
- [ ] **Exit gate:** move the real cube to 5 locations; detected coordinates plausible, marker agrees with reality, robot points only when confidence + workspace checks pass.

<details><summary>Build log</summary>

Unverified — Phases 1–2 not yet complete.

</details>

---

## PHASE 4 — Add a VLM to choose the object (not to replace geometry)

**Goal:** support instructions like "point at the blue block" while keeping metric location and motion safety in deterministic modules. The VLM answers *"which thing does the user mean?"* only — it returns a label/box/mask/grounded reference. Depth, calibration, and coordinate transforms still produce the metric target.

### Message flow

| Interface | Example payload |
|---|---|
| User → VLM | `{"instruction": "Point at the red cube", "image": RGB_frame}` |
| VLM → perception | `{"selected_object": "red cube", "region": [x1,y1,x2,y2], "confidence": 0.93}` |
| Perception → geometry | `{"mask": ..., "center_pixel": [u,v], "depth_m": 0.84}` |
| Geometry → motion | `{"frame": "base_link", "point_m": [0.51,-0.18,0.72], "confidence": 0.88}` |
| Motion → SDK | Safe target pose or approved joint trajectory |

### Checklist

- [ ] VLM choice recorded here. Note: LimX's own `FluxVLA` / OpenPI-based stack (pi0/pi0.5) is an end-to-end VLA (image+text → actions directly, no separate IK stage) — **deliberately not used here**, since it gives no guaranteed standoff distance or collision margin. Keep this as a reference for their WebSocket/robot-interface boilerplate only, not as the control architecture. See [Isaac Sim, Isaac Lab & FluxVLA Training](../software/isaac-sim-training.md) for that stack.
- [ ] Command schema documented (as above).
- [ ] Test scene and labels defined.
- [ ] Latency and memory usage recorded.
- [ ] JSON output validates against schema.
- [ ] Overlay clearly marks intended object.
- [ ] Base-frame target produced independently of VLM prose (i.e. geometry module never trusts coordinates from the VLM itself).
- [ ] Operator preview understandable before execution.
- [ ] Safety/ethics rule implemented; unsafe commands blocked.
- [ ] **Exit gate:** system follows a natural-language instruction, selects the intended visible object, produces a verified 3D base-frame target, previews the motion, and points only after all deterministic safety checks pass.

<details><summary>Build log</summary>

Unverified — Phases 1–3 not yet complete.

</details>

---

## Recommended first action

Download/import the correct TRON 2 description, create a clean writable Isaac Sim project, add one cube, verify articulation and joint mapping — **before writing any pointing controller.** The first program should only read the cube pose and print it (Task 1.3 above).

## Sources

| Source | URL |
|---|---|
| Original roadmap (archived) | `source-documents/Vision-to-Pointing Development Roadmap.docx` |
| TRON 2 robot model | `github.com/limxdynamics/robot-description` |
| Isaac Sim / Isaac Lab / FluxVLA page (this wiki) | [`software/isaac-sim-training.md`](../software/isaac-sim-training.md) |
| TRON 2 SDK Development Guide | internal — see `reference/document-sources.md` |
| TRON 2 User Manual | internal — see `reference/document-sources.md` |

*This roadmap is based on the supplied TRON 2 SDK Development Guide and User Manual, plus the LimX GitHub org. Exact SDK function names/availability must be verified against the installed firmware/SDK version before implementation.*
