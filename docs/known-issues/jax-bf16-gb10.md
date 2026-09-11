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

A known, still-open upstream bug in JAX's XLA backend on GB10/aarch64 (`sm_12.1`): `jax-ml/jax#28416`, `openxla/xla#19105`. Reproduced identically on JAX 0.7.2, 0.9.2, and 0.11.1 — a fix exists in JAX's source but hadn't reached a published wheel at time of writing. Not something we can fix on our side.

**Fix**

Disable Triton-generated GEMM kernels to route around the broken compilation path:

```bash
XLA_FLAGS="--xla_gpu_enable_triton_gemm=false" uv run scripts/serve_policy.py --profile configs/deploy/<your_profile>.yaml
```

**Related**

- `nvidia-smi` will show JAX claiming a very large share of GPU memory (e.g. ~93.7GB of 128GB) regardless of actual checkpoint size — that's JAX's default pre-allocation behavior, not a leak. Fix with `XLA_PYTHON_CLIENT_PREALLOCATE=false` if you need training and serving to coexist.
- Source: build log, Aug 28 (not yet migrated into the wiki as its own page)
