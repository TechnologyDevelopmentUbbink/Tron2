---
title: 1-4-vscode-integration
---

# Vision-to-Pointing Development Roadmap

| Item | Value |
|------|-------|
| **Author** | Arjen van Dijk |
| **Date** | 23-07-2026 |
| **Operating System** | Ubuntu 24.04 |
| **Isaac Sim** | 6.0.1 |
| **Hardware** | NVIDIA GB10 Grace Blackwell Superchip |

---

## Objective

Move Python development from the built-in Isaac Sim Script Editor to Visual Studio Code.

Using VS Code provides a full development environment with syntax highlighting, project management, version control and debugging while still executing the Python code inside the running Isaac Sim instance.

---

## Enable the Isaac Sim VS Code Integration

Open **Isaac Sim**.

Navigate to:

```text
Window → Extensions
```

Search for:

```text
isaacsim.code_editor.vscode
```

Enable the extension.

This allows Visual Studio Code to communicate directly with the running Isaac Sim instance.

![Isaac Extensions](../../assets/images/1.4Figure.png)

---

## Install the VS Code Extension

Open **Visual Studio Code**.

Open the **Extensions** marketplace.

Install:

```text
Isaac Sim VS Code Edition
```

Publisher:

```text
NVIDIA
```

---

## Create the Python Script

Create a new file:

```text
/ home/spark-ubbink/Desktop/Python vs code/move_cube.py
```

Copy the following script into the file.


??? example "move_cube.py"

    --8<-- "../../assets/code/move_cube.py"


```python
import asyncio
import omni.kit.app

from isaacsim.core.experimental.prims import XformPrim

cube = XformPrim("/World/Cube")

POSITIONS = [
    [0.5, -1.5, 0.1],
    [2.0, -1.5, 0.1],
    [2.0,  1.5, 0.1],
    [0.5,  1.5, 2.0],
    [1.0,  0.8, 0.1],
]


async def wait_seconds(seconds):
    app = omni.kit.app.get_app()
    start = asyncio.get_running_loop().time()

    while asyncio.get_running_loop().time() - start < seconds:
        await app.next_update_async()


async def move_cube():
    for i, position in enumerate(POSITIONS, start=1):
        cube.set_world_poses(positions=[position])
        print(f"Position {i}/5: {position}")
        await wait_seconds(5)

    print("Finished moving cube.")


asyncio.ensure_future(move_cube())
```

Save the file.

---

## Run the Script

Open the **Isaac Sim** extension from the left-hand activity bar in Visual Studio Code.

Open:

```text
move_cube.py
```

Click:

```text
Run
```

The script is executed directly inside the running Isaac Sim instance.

The cube should immediately move through the predefined positions while the simulation continues running.

![VS code extension run](../../assets/images/1.41Figure.png)

---

## Generate an Extension Template

Return to **Isaac Sim**.

Navigate to:

```text
Utilities → Generate Extension Templates
```

Fill in the following values.

| Field | Value |
|------|------|
| **Extension Path** | `/home/spark-ubbink/Desktop/Python vs code/Script_starting_extension` |
| **Extension Title** | `Script_starting` |
| **Description** | `This script starts all other scripts.` |

Note:
The extension must be generated inside its own dedicated folder (for example Script_starting_extension). Generating it directly into your general development directory may prevent Isaac Sim from loading the extension correctly.

Click:

```text
Generate Extension
```
![Generate Extension](../../assets/images/1.42Figure.png)

Isaac Sim creates a new extension project containing the required boilerplate for future development.

The generated project contains folders such as:

```text
config/
data/
docs/
Script_starting_python/
```

The Script_starting_python folder contains:

```text
extension.py
global_variables.py
__init__.py
scenario.py
ui_builder.py
README.md
```

This project will be used as the foundation for creating a controller that automatically starts when the simulation begins and stops when the simulation ends.

---
