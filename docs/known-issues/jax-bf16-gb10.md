---
tags:
  - DGX Spark
  - JAX
  - OpenPI
---

# bf16 crash on GB10 (JAX / Blackwell)

**Symptom**

`serve_policy.py` loads the checkpoint fine, then crashes during warmup compilation:

```
Unsupported conversion from bf16 to f16
LLVM ERROR: Unsupported rounding mode for conversion.
```

**Cause**

At the time of the August investigation, an upstream bug in JAX's XLA backend on GB10/aarch64 (`sm_12.1`): `jax-ml/jax#28416`, `openxla/xla#19105`. Reproduced identically on JAX 0.7.2, 0.9.2, and 0.11.1 — a fix exists in JAX's source but hadn't reached a published wheel at time of writing. The current upstream release status has not been rechecked for this documentation import.

**Fix**

Disable Triton-generated GEMM kernels to route around the broken compilation path:

```bash
XLA_FLAGS="--xla_gpu_enable_triton_gemm=false" uv run scripts/serve_policy.py --profile configs/deploy/<your_profile>.yaml
```

**Related**

- `nvidia-smi` will show JAX claiming a very large share of GPU memory (e.g. ~93.7GB of 128GB) regardless of actual checkpoint size — that's JAX's default pre-allocation behavior, not a leak. Pre-allocation can be configured, but our procedure keeps training and serving separate; changing that flag does not validate simultaneous use.
- Source: August 28 build-log account; the original log is not included in this import.
- [GB10 environment](../learning/lerobot-setup.md) and [policy-server operating constraints](../deployment/policy-management.md).
