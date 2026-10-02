# FluxVLA

FluxVLA remains an active route. Keep its environment, checkpoints and deployment path separate from LeRobot and LimX OpenPI.

## Software layers

LimX's stack is organized in three layers:

- **System 0** — whole-body motion foundation model
- **System 1** — VLA/WAM skills + AI infrastructure (this is where FluxVLA lives)
- **System 2** — COSA, an agent OS for LLM/world-model-based reasoning and planning

**FluxVLA Engine** is the open-source training framework for System 1: data handling, simulation training, real-robot iteration, and deployment. Supports OpenVLA, LlavaVLA, GR00T, Pi0, and Pi0.5 on Llama/Gemma/Qwen backbones.

!!! warning "Isaac Sim support status"
    Native Isaac Sim support is listed as an open TODO item in the FluxVLA repository itself. Training data currently comes mainly from LIBERO (MuJoCo-based) and real-robot demonstrations. Isaac Sim/Isaac Lab is a separate, parallel path — not a built-in part of FluxVLA.

- Repo: [`limxdynamics/FluxVLA`](https://github.com/limxdynamics/FluxVLA)
- Docs: `fluxvla.limxdynamics.com`


## Checkpoint compatibility

[FluxVLA and tron2_openpi checkpoints are not interchangeable](../known-issues/checkpoint-format-mismatch.md). A shared architecture name does not imply matching parameter names or runtime transforms. Our LeRobot/OpenPI state layout also differs from the FluxVLA order; see [Joint layouts](../reference/joint-layouts.md).

## Sources

[Original stack overview](../software/isaac-sim-training.md#sources); the August checkpoint investigation. The framework support list above is a source snapshot, not a claim that every route has been tested here.
