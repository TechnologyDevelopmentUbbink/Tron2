# Viewer and camera-mapping pitfalls

**Rerun only shows welcome:** use the full viewer address with the data-server parameter. A web page loading does not prove dataset delivery.

**A wrist camera is missing from SmolVLA:** select one overview and both wrists explicitly. Mapping two stereo-head streams can consume the three-camera budget.

**Policy launcher rejects ACT:** the first ACT model used five cameras; the measured runtime provides three. Match the model and live features instead of bypassing validation.

**Viewer remains after stopping:** the Python launcher can leave its child process alive. Check the actual viewer process.

[Viewer procedure](../learning/dataset-viewer.md) · [Model camera requirements](../learning/act-and-smolvla.md#cameras-must-match-deployment).

**Source:** UBB-IL-001 sections 6.3, 8.8 and 13.3, [source register](../reference/document-sources.md).
