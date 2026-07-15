# Software installation

The official low-level SDK repository supplies platform-specific Python wheels and C++ libraries. Install into an isolated development environment and pin the repository commit used by the project.

## Supported platforms in the SDK guide

- Linux x86-64
- Linux AArch64
- Windows for the Python package

## Obtain the SDK

```bash
git clone https://github.com/limxdynamics/limxsdk-lowlevel.git
cd limxsdk-lowlevel
git rev-parse HEAD
```

Install the wheel from the directory matching the computer architecture and Python environment. Use the current repository README for the exact path and requirements.

!!! warning "Do not connect to hardware during package validation"

    First verify imports, architecture, message types, and simulation/example behavior without a live motion-command path.

## Verification record

| Item | Value |
| --- | --- |
| Repository commit | Not pinned |
| OS/architecture | Not recorded |
| Python/C++ toolchain | Not recorded |
| Robot model | Not recorded |
| Simulation test | Not performed |
| Hardware test approval | Not granted |

## Sources

- [limxsdk-lowlevel](https://github.com/limxdynamics/limxsdk-lowlevel)
- LimX Dynamics, *TRON 2 SDK Development Guide*, v0.5, sections 2.1.2 and 2.2.2.
