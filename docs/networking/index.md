# Networking

The robot uses networking for the information page, developer computer, SDK communication, VR teleoperation, and file/software transfer.

!!! warning "No credentials or fixed addresses in the public wiki"

    The official manuals include factory-default credentials and fixed private addresses. They are intentionally omitted here. Obtain the approved values from the controlled source or robot owner and change defaults where supported.

## Connection paths

| Path | Use | Verification |
| --- | --- | --- |
| Robot Wi-Fi hotspot | Setup, information page, developer access, VR | Confirm SSID belongs to the intended robot without publishing it |
| Wired Gigabit Ethernet | Stable development connection | Use an approved isolated interface/profile |
| Developer computer SSH | Command-line development | Use named accounts/managed credentials; do not place secrets in docs |
| SDK transport | Low/high-level robot communication | Confirm model, target, and environment before sending commands |

## Safe setup workflow

1. Identify the target robot physically.
2. Disconnect unrelated networks if required by the test plan.
3. Obtain the current network profile from the controlled source.
4. Configure only the intended PC interface.
5. Test basic reachability without commanding motion.
6. Confirm the robot information/model before starting an SDK or VR session.
7. Record the configuration in a non-public asset register.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| No Wi-Fi entry | Robot power/state, distance, correct band, nearby similarly named robots |
| Link but no application connection | Target identity, PC subnet/profile, firewall, service state, application version |
| Intermittent control | Signal quality, competing networks, power saving, cable/connector, packet loss |
| SSH rejected | Approved account, key/credential, host identity, access policy; never paste secrets into an issue |

## Sources

- LimX Dynamics, *TRON 2 User Manual*, v0.1, sections 5.3 and 6.
- LimX Dynamics, *TRON 2 SDK Development Guide*, v0.5, sections 1.1–1.3.
