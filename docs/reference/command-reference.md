# Local workflow command glossary

These names refer to tools maintained in the active local robot project. This documentation repository does not ship them. Use the operator's current installation and help output for exact arguments.

| Utility | Purpose | What to verify |
| --- | --- | --- |
| `controleer` | Check a dataset | Format, complete episodes, layout, statistics and state/action semantics |
| `bekijk` | View an episode | Images and curves agree; browser connected to the data server |
| `train-act` | Train ACT | Correct dataset and saved split |
| `train-smolvla` | Fine-tune SmolVLA | Three-camera mapping, task text and base-model availability |
| `beoordeel` | Compare held-out predictions | Same test set; oracle/hold self-checks pass |
| `proeven` | Score real trials | Defined task, conditions, counts and uncertainty |
| `maak_schone_kopie.py` | Repair supported recording defects in a copy | Original preserved; gaps within limits; video alignment unchanged |
| `converteer_v21.sh` | Convert an older dataset using a copy | Do not run an in-place conversion on the sole original |
| `controleer_installatie.py` | Verify GPU/video environment | Known video frames and negative checks |
| `zet-policy-neer` | Package a trained policy locally | Weights, task text and split provenance |
| `start-server` | List/select a policy server | Selected policy identity and completed warm-up |
| `beginstand_uit_opnames.py` | Compare recorded start-pose candidates | Limits and route assessed for that cell |

Dutch output: **klaar** = ready; **let op** = warnings; **NIET TRAINEN** = do not train; **GEREED** = ready after warm-up; **JA** = operator confirmation; **ROBOT BEWOOG NIET** = no observed movement.

For building this wiki itself, install `requirements-docs.txt` and use `python -m mkdocs serve`. Validate with `python -m mkdocs build --strict` before publishing.

**Source:** [UBB-IL-001](document-sources.md), sections 2, 5–9; [UBB-CLIENT-001](document-sources.md), sections 16.5–16.6.
