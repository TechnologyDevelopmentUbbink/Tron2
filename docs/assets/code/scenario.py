"""Main TRON2 extension controller."""

from .cube_demo import CubeDemo


class Tron2Controller:
    """Manage the enabled TRON2 simulation modules."""

    def __init__(self) -> None:
        self._running = False
        self._step_count = 0
        self._print_timer = 0.0

        self._cube_demo_enabled = True
        self._cube_demo = CubeDemo()

    @property
    def running(self) -> bool:
        return self._running

    @property
    def cube_demo_enabled(self) -> bool:
        return self._cube_demo_enabled

    def set_cube_demo_enabled(self, enabled: bool) -> None:
        """Enable or disable the cube demo."""
        self._cube_demo_enabled = bool(enabled)

        print(
            "[TRON2] Cube demo switch: "
            f"{'ON' if self._cube_demo_enabled else 'OFF'}"
        )

        # Allow the switch to be changed while simulation is running.
        if self._running:
            if self._cube_demo_enabled:
                self._cube_demo.start()
            else:
                self._cube_demo.stop()

    def start(self) -> None:
        """Called when the Isaac Sim timeline starts."""
        if self._running:
            return

        self._running = True
        self._step_count = 0
        self._print_timer = 0.0

        print("[TRON2] Controller started")

        if self._cube_demo_enabled:
            self._cube_demo.start()

    def update(self, step: float) -> None:
        """Called once per physics step."""
        if not self._running:
            return

        self._step_count += 1
        self._print_timer += float(step)

        if self._cube_demo_enabled:
            self._cube_demo.update(step)

        if self._print_timer >= 1.0:
            print(
                f"[TRON2] Running - physics steps: "
                f"{self._step_count}"
            )
            self._print_timer = 0.0

    def stop(self) -> None:
        """Called when the Isaac Sim timeline stops."""
        if not self._running:
            return

        self._cube_demo.stop()
        self._running = False

        print(
            f"[TRON2] Controller stopped after "
            f"{self._step_count} physics steps"
        )

    def reset(self) -> None:
        """Reset all controller modules."""
        self._cube_demo.reset()

        self._running = False
        self._step_count = 0
        self._print_timer = 0.0

    def cleanup(self) -> None:
        """Clean up when the extension closes or reloads."""
        self.stop()
        self._cube_demo.reset()
