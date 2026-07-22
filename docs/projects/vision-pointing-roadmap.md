---
title: Vision-to-Pointing Development Roadmap
---

# Vision-to-Pointing Development Roadmap

Source status: internal project plan, partly Unverified until each phase is executed. Not yet Ubbink-verified end to end.

This page is a living build log, not a fixed spec. Each checklist item gets updated in place as work happens: software/version used, what worked, what didn't, dead ends. If the project stalls at any phase, this page should still stand on its own as a usable record for whoever picks it up next (including future-you).

Primary first use case: place a coloured cube in front of the robot and make one arm point toward it without touching it.

## How the complete system will eventually work

The final system is not one giant AI model. It is a chain of small modules. Each one takes a simple input and hands off a simple, well-defined output to the next one:

```
Camera frame (RGB+D) → Target selection → 3D position (camera frame)
  → Coordinate transform (→ robot base) → Pointing pose → IK/motion planner
  → TRON 2 SDK robot command
```

### Official SDK facts used in this guide

- The TRON 2 SDK talks to the simulator at `127.0.0.1` and the real robot at `10.192.1.2` — different addresses, don't mix them up.
- The SDK gives you the robot's joint angle (`q`), joint speed (`dq`), and estimated torque (`tau`).
- The EDU compute module is where your own code runs and talks to the robot controller over the robot's network.

### Robot model for Isaac Sim

See: [Isaac Sim, Isaac Lab & FluxVLA Training → Robot model (URDF/USD)](../software/isaac-sim-training.md#robot-model-urdfusd-for-isaac-sim) for the `limxdynamics/robot-description` repo.

---

## Project steps

| Phase | What changes |
|---|---|
| 1. Simulation | Fake cube, fake robot — just prove the math and motion work |
| 2. Real control | Same motion, but on the real TRON 2. Target is still a number you type in |
| 3. Camera | A real camera finds the real cube instead of you typing in a number |
| 4. VLM | You can say what to point at instead of it always being "the cube" |

---

## **PHASE 1** — Simulated cube → simulated TRON 2 points at it

**Goal:** learn Isaac Sim and prove the geometry + arm-motion chain work, before any camera or real robot is involved.

**Data contract:** input = exact cube position from the Isaac stage. Output = simulated joint targets and a visible pointing pose. No camera, no VLM, no real robot.

### Checklist

#### 1.1 — Get the robot model into a working Isaac Sim project

- [x] Clone `limxdynamics/robot-description`, pick the TRON 2 variant that matches your actual hardware (dual-arm/desktop). See linked page above for exact steps.
- [x] Open the scene — it should load with no missing-file errors.
- [x] Check the robot has all its expected joints/links, and that the **Articulation Root** is set. (If this is wrong, the robot will look fine but physics silently won't work)

[Phase 1.1 – Robot Import & Initial Scene Setup](../assets/Results_Project_Cube/1-1-robot-import-initial-scene-setup.md)

#### 1.2 — Confirm you know which joint is which

- [x] Write down which joint name in the model = which real joint (left arm, right arm, which DOF, in what order).
- [x] Move the cube by typing in numbers (not just dragging it) — confirm you can do this.
- [x] Pick one clear point on the arm that counts as "where it's pointing from" (e.g. gripper centre) and write down why you picked it.

[Phase 1.2 – Robot reference Cube](../assets/Results_Project_Cube/1-2-robot-inspection-reference-scene.md)

#### 1.3 — Read the cube's position and print it (still no motion)

- [ ] Write a small script that only reads the cube's `[x,y,z]` and prints it. Nothing moves yet.
- [ ] Move the cube around and confirm the printed numbers actually change to match.

#### 1.4 — Convert cube position to "relative to the robot"

- [ ] Convert the cube's world position into "position relative to the robot's base."
- [ ] Check it by hand: put the cube a known distance in front of the robot (e.g. 30 cm), confirm the converted number roughly says 30 cm.

#### 1.5 — Work out where the arm should point to

- [ ] Compute a target point a little *before* the cube, not on top of it: `pointer_position = cube_position - safety_offset × pointing_direction`.
- [ ] Pick a safety offset distance and write it down (start safe: 20–30 cm).
- [ ] Show a visible marker at that computed point, in front of the cube.

#### 1.6 — Get the arm to actually move there

- [ ] **Decide:** pick an IK solver (Lula IK or cuRobo) and write down which one and why. Check what LimX's own Isaac Lab repos default to first — matching them may save you pain later.
- [ ] **Check:** the arm reaches the point without going past its joint limits.
- [ ] **Check:** the arm doesn't hit itself or touch the cube on the way there.

#### 1.7 — Phase 1 exit gate

- [ ] Move the cube to **5 different spots** — the arm points correctly and repeatably every time.
- [ ] Save a short video of this.
- [ ] Save the 5 coordinates you tested, next to the video.

---

## **PHASE 2** — First real-robot test (target still typed in)

**Goal:** get the real TRON 2 to do the same small, safe pointing motion. You still type in the target by hand — no camera yet.

**Preferred way in:** use a high-level move command (Cartesian/ServoJ/end-pose) if LimX gives you one. Only use raw 300 Hz joint commands if there's no other option — that path is powerful but unforgiving.

### Checklist

#### 2.1 — Connect, but don't move anything yet

- [ ] Connect to the robot, ping it, print motor count and the `q`/`dq`/`tau` stream. **The robot must not move for this step.**

#### 2.2 — Safety prep

- [ ] Write down the emergency-stop procedure and actually practice it before anything moves.
- [ ] Write down the workspace limits — the exact box/area the arm is allowed to move in during testing.

#### 2.3 — Make sure sim and real agree

- [ ] Check that the joint order/names in Isaac match the joint order/names the real SDK uses.
- [ ] Try the high-level move interface once, with something trivial.

#### 2.4 — First real movement, small and safe

- [ ] Command one small pose change and confirm it works.
- [ ] Keep logging robot state while it moves; save what you see, even if nothing went wrong.

#### 2.5 — Full pointing motion, with a typed-in target

- [ ] Type in a target position (in robot-base coordinates), log the pose you calculated *before* you send it, then execute.

#### 2.6 — Phase 2 exit gate

- [ ] The real robot points at 3 different typed-in targets, staying inside the workspace limits you wrote down. It should be repeatable, easy to watch, and easy to stop.

---

## **PHASE 3** — Real camera finds the real cube

**Goal:** stop typing in the target — let a real camera find the cube instead. Everything after that point is identical to Phase 2.

### Checklist

#### 3.1 — Get the camera working

- [ ] Decide which camera (RealSense vs. TRON 2's built-in one) and write it down.
- [ ] Save one matched colour + depth image, and record the camera's calibration numbers (`fx, fy, cx, cy` and depth scale).

#### 3.2 — Find the cube in the image

- [ ] Detect the cube (simplest option: colour thresholding) and get its centre pixel.
- [ ] Read the depth at that pixel; throw away the reading if it's missing, zero, or clearly wrong.

#### 3.3 — Turn that pixel into a real 3D point

- [ ] Convert pixel + depth into an actual `[X,Y,Z]` point in metres, from the camera's point of view. Confirm it stays stable across a few frames (not jumping around).

#### 3.4 — Line up the camera with the robot

- [ ] Do a camera-to-robot calibration (hand-eye calibration) — this step usually takes longer than you expect, budget real time for it.
- [ ] Convert the camera-frame point into robot-base coordinates and print it.

#### 3.5 — Double check before letting it move

- [ ] Show the computed point as a marker in Isaac/RViz and compare it to where the cube actually is in real life.
- [ ] Test across 5 real positions, write down the results, and explain anything that doesn't match.
- [ ] Make the system refuse to move if it's not confident in the detection.

#### 3.6 — Phase 3 exit gate

- [ ] Move the real cube to 5 spots. Every time: the detected position makes sense, matches reality, and the robot only points when it's confident.

---

## **PHASE 4** — Let a VLM pick what to point at

**Goal:** support instructions like "point at the blue block" or "point at a person" — but the actual position/motion math stays exactly as safe and deterministic as before. The VLM's only job is answering "which thing do they mean?" — it never gives a coordinate.

| Step | Example |
|---|---|
| You → VLM | "Point at the red cube" + the camera image |
| VLM → rest of system | "That's the red cube, here's roughly where it is in the image, I'm 93% sure" |
| Rest of system → geometry | exact pixel + depth of that object |
| Geometry → motion | the real 3D point in robot-base coordinates |
| Motion → robot | the actual safe move command |

### Checklist

#### 4.1 — Pick a VLM and agree on its output format

- [ ] Pick a VLM, write down which one, and define exactly what it should return (label, region, confidence — nothing more).

#### 4.2 — Reuse everything from Phase 3

- [ ] Feed the VLM's chosen region into the *same* detection/geometry pipeline from Phase 3 — don't build a new one.
- [ ] Make sure the geometry step never trusts a coordinate from the VLM directly — only from the same measured pipeline as before.

#### 4.3 — Add the safety net

- [ ] Measure how slow this is (latency) and how much memory it uses.
- [ ] Show what the system thinks you meant before it moves (an overlay on the image is enough).
- [ ] If the VLM isn't confident, or picks something ambiguous, refuse to move.

#### 4.4 — Phase 4 exit gate

- [ ] Say a plain instruction → correct object gets picked → a real, checked 3D position comes out → the robot only points once every safety check passes.

Note: LimX has its own end-to-end system (FluxVLA / OpenPI, pi0/pi0.5) that skips all this and goes straight from image+text to motion. Not using that here on purpose — it can't guarantee a safe stand-off distance the way this step-by-step version can. Worth knowing about for other projects though: [Isaac Sim, Isaac Lab & FluxVLA Training](../software/isaac-sim-training.md).

---
