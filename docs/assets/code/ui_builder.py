"""TRON2 controller UI."""

import omni.timeline
import omni.ui as ui
import omni.usd
from omni.usd import StageEventType

from .scenario import Tron2Controller


class UIBuilder:
    """Connect the TRON2 controller to Isaac Sim events."""

    def __init__(self) -> None:
        self._controller = Tron2Controller()

        self._status_label = None
        self._cube_status_label = None
        self._cube_demo_model = None

    def on_menu_callback(self) -> None:
        """Called when the extension window is opened."""
        pass

    def on_timeline_event(self, event: object) -> None:
        """Handle Isaac Sim Play and Stop events."""
        if event.event_name == omni.timeline.GLOBAL_EVENT_PLAY:
            self._controller.start()
            self._set_controller_status("Running")

        elif event.event_name == omni.timeline.GLOBAL_EVENT_STOP:
            self._controller.stop()
            self._set_controller_status("Stopped")

    def on_physics_step(self, step: float) -> None:
        """Update the controller every physics step."""
        self._controller.update(step)

    def on_stage_event(self, event: object) -> None:
        """Reset the controller when the stage changes."""
        opened_event = omni.usd.get_context().stage_event_name(
            StageEventType.OPENED
        )
        closed_event = omni.usd.get_context().stage_event_name(
            StageEventType.CLOSED
        )

        if event.event_name in (opened_event, closed_event):
            self._controller.reset()
            self._set_controller_status("Ready")

    def build_ui(self) -> None:
        """Build the TRON2 extension window."""
        with ui.VStack(spacing=10, height=0):
            ui.Label("TRON2 Controller")
            ui.Separator()

            self._status_label = ui.Label("Status: Ready")

            ui.Spacer(height=5)

            with ui.HStack(height=24, spacing=8):
                ui.Label("Cube movement", width=150)

                self._cube_demo_model = ui.SimpleBoolModel(
                    self._controller.cube_demo_enabled
                )

                ui.CheckBox(
                    model=self._cube_demo_model,
                    width=24,
                    height=24,
                )

            self._cube_demo_model.add_value_changed_fn(
                self._on_cube_demo_switch_changed
            )

            self._cube_status_label = ui.Label(
                self._cube_status_text()
            )

            ui.Spacer(height=5)

            ui.Label(
                "Press Play to start enabled modules.\n"
                "Press Stop to stop them."
            )

    def cleanup(self) -> None:
        """Clean up when the window closes or extension reloads."""
        self._controller.cleanup()

        self._status_label = None
        self._cube_status_label = None
        self._cube_demo_model = None

    def _on_cube_demo_switch_changed(self, model: object) -> None:
        enabled = model.get_value_as_bool()

        self._controller.set_cube_demo_enabled(enabled)
        self._set_cube_status()

    def _set_controller_status(self, status: str) -> None:
        if self._status_label is not None:
            self._status_label.text = f"Status: {status}"

    def _set_cube_status(self) -> None:
        if self._cube_status_label is not None:
            self._cube_status_label.text = self._cube_status_text()

    def _cube_status_text(self) -> str:
        if not self._controller.cube_demo_enabled:
            return "Cube demo: Disabled"

        if self._controller.running:
            return "Cube demo: Running"

        return "Cube demo: Enabled"
