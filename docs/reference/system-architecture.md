# System Architecture — Hardware, Software & Communication

Source status: internet-sourced, unofficial. Compiled from LimX and NVIDIA public documentation; not yet Ubbink-verified.

Overview of which software runs where, and how the pieces of a full TRON 2 EDU + Isaac Sim/Lab + DGX Spark setup talk to each other.

![TRON 2 system architecture diagram](../assets/tron2-system-architecture.png)

## Components

| Component | Role | Key software |
|---|---|---|
| **NVIDIA DGX Spark** | Training & inference hardware | Isaac Lab (RL training), FluxVLA (VLA training), OpenPI policy server (live inference) |
| **Pico 4 Ultra Enterprise** | VR headset | LimX teleop-app — sends handtracking/control commands straight to the TRON2 computebox |
| **Separate workstation** *(optional, sim-teleop only)* | RTX PRO 6000 / RTX 5090-class, **not** the DGX Spark | Isaac Sim + Isaac Lab, CloudXR Runtime (Docker) |
| **TRON 2 EDU computebox** | Intel Core i7-1165G7, 2TB storage | LimX teleop-app receiver / Isaac Teleop client, ONNX runtime (local RL policies), OpenPI WebSocket client |
| **TRON 2 — arms & actuators** | Motors/servos, dual-arm | No onboard "smart" software — pure actuation, receives real-time joint commands from the computebox |
| **`robot-description` repo** | Shared files | URDF/xacro, USD (Isaac Sim), MuJoCo XML — one model used consistently across workstation, DGX Spark, and the physical robot |

## Connections

| # | Connection | Protocol | Notes |
|---|---|---|---|
| 1 | DGX Spark ↔ TRON2 computebox | WebSocket (OpenPI protocol) | Live VLA inference: robot sends camera/joint data, receives actions back |
| 2 | Pico 4 Ultra ↔ TRON2 computebox | LimX teleop-app / local WiFi | Teleoperation directly on the physical robot — no workstation needed |
| 3 | Pico 4 Ultra ↔ separate workstation | NVIDIA CloudXR (Docker, OpenXR) | Optional: teleoperating inside the Isaac Sim simulation instead of the real robot |
| 4 | Separate workstation ↔ DGX Spark | Network (optional, Kubernetes) | Only relevant when scaling to multiple users/teleop sessions |
| 5 | `robot-description` → workstation, DGX Spark, TRON2 | File import (local/git clone) | Same robot model kept consistent everywhere |
| 6 | Computebox ↔ arms/actuators | **EtherCAT (wired)** | Real-time motor control — a fixed, physical connection inside the robot itself, not WiFi |

!!! danger "DGX Spark cannot run XR teleoperation"
    Connections 2 and 3 are separate paths for a reason: XR/CloudXR teleoperation is not supported on the DGX Spark itself (encoding performance limitation, confirmed in current Isaac Lab docs). Simulation teleoperation with a VR headset always requires the separate RTX-class workstation (connection 3); the DGX Spark is used for training and for serving the trained policy (connection 1), not for rendering XR sessions.

See [Isaac Sim, Isaac Lab & FluxVLA Training](../software/isaac-sim-training.md) for details on each path.
