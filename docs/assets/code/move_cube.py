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
