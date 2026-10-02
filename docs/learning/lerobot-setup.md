# LeRobot on GB10

**Measured environment:** ASUS Ascent GX10 and DGX Spark, 28–30 September 2026. Keep this environment separate from Isaac Lab and from the JAX/OpenPI server.

## The working combination

| Component | Tested version |
| --- | --- |
| Ubuntu / architecture | 24.04 / aarch64 |
| Python | 3.12.3 |
| NVIDIA driver | 580.173.02, R580 |
| LeRobot | 0.6.1, training + SmolVLA + viewer |
| PyTorch / torchvision | 2.11.0+cu130 / 0.26.0+cu130 |
| TorchCodec | 0.11.1+cu130 |
| PyAV | 15.1.0 |
| NumPy / transformers | 2.2.6 / 5.5.4 |
| Rerun / TensorBoard | 0.33.1 / 2.21.0 |
| System FFmpeg | 6.1.1 |

The measured environment lives in a host virtual environment on internal NVMe. The CUDA wheels bring their own runtime; installing them did not require changing the NVIDIA driver. The local package freeze is the reproducibility record.

## Why the Isaac Lab container was a dead end

The inspected container had Python 3.11.13, PyTorch 2.9, NumPy 1.26 and transformers 4.57.6. LeRobot 0.6.1 needs a newer Python and incompatible dependency versions. Matching TorchCodec 0.8/0.9 aarch64 wheels were unavailable. Installing into a container launched with `--rm` also loses the changes when it exits.

These are properties of the inspected versions, not a permanent rule about containers. A future derived image needs a fresh compatibility check.

## Verify the environment, not just the import

The local installation check confirms CUDA works and that LeRobot actually selects TorchCodec. It encodes a known AV1 test video and checks five timestamps with both TorchCodec and PyAV. A deliberately shifted expectation must fail.

TorchCodec needs the system FFmpeg shared libraries. PyAV bundles its own; a working PyAV import does not prove TorchCodec works. LeRobot can otherwise fall back to PyAV with only a warning. Training explicitly requests TorchCodec so an unavailable backend cannot pass unnoticed.

The installer needed a longer download timeout for large CUDA wheels. The first SmolVLA fine-tune needs Hub access for the base model and processor files; cached deployment can subsequently work offline.

## Sharing the GPU

Run long trainings sequentially. Do not run a training alongside Isaac Sim or a policy server. The recorded shared-GPU run was roughly twice as slow. Keep the R580 renderer-compatible setup until a replacement driver is validated for both learning and simulation.

For a second machine: reproduce the freeze, run the installation check and complete the practice-data workflow before diagnosing real recordings.

**Source:** [UBB-IL-001](../reference/document-sources.md), sections 3, 6.1, 9 and 14.1. [Environment pitfalls](../known-issues/lerobot-environment.md).
