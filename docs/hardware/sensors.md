# Cameras and sensors

Sensor availability depends on configuration and on whether the source describes physical hardware or only model geometry.

| Sensor or frame | Official source coverage | Notes |
| --- | --- | --- |
| IMU | User manual and robot-description repository | Present across documented variants; exact frame/model varies |
| Waist RGB-D camera | User manual | Listed for both EDU and standard editions |
| Head RGB-D camera | User manual | Listed for the EDU dual-arm configuration |
| Wrist RGB-D cameras | User manual | Listed for the EDU dual-arm configuration |
| Chest D435-style frame | robot-description repository | Geometry/frame representation; simulation plugin support varies |
| YG peripheral stack | robot-description repository | Variant-specific modeled links and documented physical peripherals |

!!! warning "Model is not proof of installed hardware"

    A URDF link or mesh does not prove that a sensor is installed, powered, calibrated, or supported by a driver on the Ubbink robot.

## Sources

- LimX Dynamics, *TRON 2 User Manual*, v0.1, section 1.2.
- [LimX TRON 2 robot-description repository](https://github.com/limx-tron2/robot-description), variant and sensor overview.



## Streams observed in the learning/deployment work

The first real dataset contained five camera streams. The measured deployment selects one overview and two wrist streams (cam_high, cam_left_wrist, cam_right_wrist). The supplied pipeline diagram records 640 × 480 for the overview and 848 × 480 for the wrists.

These stream observations do not complete the physical sensor model/driver inventory. [Observation pipeline](../reference/observation-pipeline.md) and [dataset camera mapping](../learning/act-and-smolvla.md#cameras-must-match-deployment).
