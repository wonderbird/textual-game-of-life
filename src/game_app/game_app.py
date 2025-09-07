from textual.app import App, ComposeResult
from textual.widgets import Log, Footer, Header
from game_app.textual_universe_view import TextualUniverseView
from game_app.universe_view import UniverseView


class GameApp(App):
    CSS_PATH = "style.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("n", "produce_next_generation", "Next generation"),
        ("r", "reset_to_seed", "Reset to seed"),
    ]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._universe_view: UniverseView | None = None

    def compose(self) -> ComposeResult:
        yield Header()
        yield Log(id="universe")
        yield Footer()

    def on_mount(self) -> None:
        self.log("We can send log messages to the textual console now.")

    def on_ready(self) -> None:
        self._universe_view = TextualUniverseView(self)
        self.action_reset_to_seed()

    def action_produce_next_generation(self) -> None:
        self._universe_view.on_produce_next_generation()

    def action_reset_to_seed(self) -> None:
        self._universe_view.on_reset_to_seed()

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = GameApp()
    app.run()
