# Batteries and charging

!!! danger "Use the supplied equipment and official procedure"

    Battery charging can create electrical, fire, and mechanical hazards. Confirm the battery/charger belongs to the installed configuration and inspect it before use. This summary does not replace the official manual.

## Published values

| Item | Official manual value | Applies to |
| --- | --- | --- |
| Main battery type | Ternary lithium | EDU and standard editions in the cited manual |
| Nominal output | 46.8 V | Main robot battery |
| Capacity | 9 Ah | Main robot battery |
| Charger input | 100–240 V AC, 8 A | Supplied charger |
| Charger output | 54.275 V DC, 10 A | Supplied charger |
| Published charge time | 20–80%: 30 min; 20–100%: 54 min | Manual reference value, not Ubbink verified |
| Battery swap support | Yes | Both editions in the manual |

!!! info "Official source — not yet Ubbink verified"

    Values above are paraphrased from the TRON 2 User Manual v0.1, section 1.2. Check labels on the actual Ubbink hardware before relying on them.

## Before charging

1. Stop operation and follow the approved shutdown sequence.
2. Check the battery, connector, cable, and charger for damage, contamination, heat, or swelling.
3. Confirm the charger label matches the battery and local mains supply.
4. Use a supervised, suitable charging area.
5. If anything differs from the manual or equipment label, stop and escalate.

## Remote controller

The manual describes charging the handheld controller from a 5 V / 1 A supply. A steady green controller indicator means charging is active or complete; no light means it is not charging. This indication does not distinguish active charging from completion.

## Mobile chassis

The mobile dual-arm configuration has a separate chassis battery and charger. Treat its values and procedure separately from the main TRON 2 battery.

## Source

LimX Dynamics, *TRON 2 User Manual*, TRON 2 EDU edition, v0.1, 11 June 2026, sections 1.2 and 2.
