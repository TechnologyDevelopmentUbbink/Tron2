"""Repeating cube movement demo for TRON2."""

from isaacsim.core.experimental.prims import XformPrim


class CubeDemo:
    """Move /World/Cube through a repeating list of positions."""

    CUBE_PATH = "/World/Cube"
    MOVE_INTERVAL_SECONDS = 0.8

    POSITIONS = [
        [0.5, -1.0, 0.1],
        [1, -0.5, 0.1],
        [0.7, 1, 0.1],
        [0.5, 0.2, 0.5],
        [1.0, 0.8, 0.1],
    ]

    def __init__(self) -> None:
        self._cube = None
        self._running = False
        self._elapsed_time = 0.0
        self._position_index = 0

    def start(self) -> None:
        """Start or restart the repeating cube movement."""
        if self._running:
            return

        try:
            self._cube = XformPrim(self.CUBE_PATH)
        except Exception as error:
            self._cube = None
            print(f"[TRON2] Could not access {self.CUBE_PATH}: {error}")
            return

        self._running = True
        self._elapsed_time = 0.0
        self._position_index = 0

        self._move_to_current_position()

        print("[TRON2] Cube demo started")

    def update(self, step: float) -> None:
        """Advance the cube demo using Isaac Sim physics time."""
        if not self._running or self._cube is None:
            return

        self._elapsed_time += float(step)

        if self._elapsed_time < self.MOVE_INTERVAL_SECONDS:
            return

        self._elapsed_time = 0.0
        self._position_index = (
            self._position_index + 1
        ) % len(self.POSITIONS)

        self._move_to_current_position()

    def stop(self) -> None:
        """Stop cube movement."""
        if self._running:
            print("[TRON2] Cube demo stopped")

        self._running = False
        self._elapsed_time = 0.0
        self._cube = None

    def reset(self) -> None:
        """Reset the internal demo state."""
        self.stop()
        self._position_index = 0

    def _move_to_current_position(self) -> None:
        if self._cube is None:
            return

        position = self.POSITIONS[self._position_index]

        try:
            self._cube.set_world_poses(positions=[position])
            print(
                f"[TRON2] Cube position "
                f"{self._position_index + 1}/{len(self.POSITIONS)}: "
                f"{position}"
            )
        except Exception as error:
            print(f"[TRON2] Cube movement failed: {error}")
            self.stop()
