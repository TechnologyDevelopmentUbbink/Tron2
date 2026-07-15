# ROS 2 and robot models

The SDK guide states that its documented developer computer includes ROS 2 Foxy and ROS 1 Noetic. Treat that as a source snapshot, not a universal requirement; verify the installed image before choosing packages.

## Robot-description package

The public `limx-tron2/robot-description` repository is a ROS package containing variant-specific URDF/Xacro, MuJoCo XML, meshes, and some USD assets.

```text
robot-description/
├── CMakeLists.txt
├── package.xml
└── tron2/
    └── <VARIANT>/
        ├── urdf/
        ├── xacro/
        ├── xml/
        ├── meshes/
        └── usd/        # selected variants
```

## Variant selection

Do not select a model based only on appearance. Match the robot’s recorded model identifier to the repository variant, then check branch/commit and installed modules. The repository warns that real hardware can include devices not represented in the model.

## Coordinate convention

The repository documents ROS-style axes (`x` forward, `y` left, `z` up) unless the integration stack says otherwise. It also documents special zero-versus-control-posture considerations for some leg variants. Controllers must not infer offsets without the applicable variant documentation.

## Reproducibility record

| Component | Version/commit |
| --- | --- |
| Robot model identifier | Not recorded |
| `robot-description` commit | Not pinned |
| ROS distribution | Not verified |
| SDK version | Not verified |
| Firmware set | Not verified |

## Source

[LimX TRON 2 robot-description repository](https://github.com/limx-tron2/robot-description) and LimX Dynamics, *TRON 2 SDK Development Guide*, v0.5, section 1.3.
