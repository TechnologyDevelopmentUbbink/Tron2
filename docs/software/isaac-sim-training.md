# Isaac Sim, Isaac Lab & FluxVLA

The stack overview now has focused pages:

- [Simulation overview](../simulation/index.md)
- [Robot models and Isaac Lab](../simulation/models-and-isaac-lab.md)
- [FluxVLA](../simulation/fluxvla.md)
- [Simulation and physical teleoperation](../simulation/teleoperation.md)
- [Imitation learning with LeRobot](../learning/index.md)
- [Running policies](../deployment/index.md)

The earlier overview described a policy client on the onboard computebox. In the measured September/October deployment, both policy server and client run on the Spark. See [Current architecture](../reference/system-architecture.md).

## Sources

| Source | URL |
|---|---|
| Robot model (URDF/USD/MuJoCo) | `github.com/limxdynamics/robot-description` |
| FluxVLA Engine | `github.com/limxdynamics/FluxVLA` |
| FluxVLA docs | `fluxvla.limxdynamics.com` |
| All LimX repos | `github.com/limxdynamics` |
| Isaac Lab docs | `isaac-sim.github.io/IsaacLab` |
| Isaac Lab CloudXR guide | `isaac-sim.github.io/IsaacLab/main/source/how-to/cloudxr_teleoperation.html` |
| Isaac Teleop (NVIDIA/PICO) | `github.com/NVIDIA/IsaacTeleop` |
| Isaac ROS Teleop | `github.com/NVIDIA-ISAAC-ROS/isaac_ros_teleop` |
| OpenPI | `github.com/Physical-Intelligence/openpi` |
| DGX Spark + Isaac install guide | `learn.arm.com/learning-paths/laptops-and-desktops/dgx_spark_isaac_robotics/` |

*Repo names and framework details change frequently (active development, mid-2026). Verify against current docs before cloning/installing.*
