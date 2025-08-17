from textual.app import App, ComposeResult
from textual.widgets import Log, Footer, Header


class Cell:
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    def get_x() -> int:
        return self._x

    def get_y() -> int:
        return self._y


class UniverseView:
    def __init__(self, app: App) -> None:
        self._log = app.query_one(Log)
        self._cells = []
        self.update()

    def update(self) -> None:
        self._log.clear()
        self._log.write_line(" 123456789")
        self._log.write_line("1         1")
        self._log.write_line("2         2")
        self._log.write_line("3         3")
        self._log.write_line("4         4")
        self._log.write_line("5         5")
        self._log.write_line(" 123456789")

        for cell in self._cells:
            pass


class GameApp(App):
    CSS_PATH = "style.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("n", "produce_next_generation", "Next generation"),
        ("r", "reset_to_seed", "Reset to seed"),
    ]

    def __init__(self) -> None:
        super().__init__(self)
        self._universe_view = None

    def compose(self) -> ComposeResult:
        yield Header()
        yield Log(id="universe")
        yield Footer()

    def on_ready(self) -> None:
        self._universe_view = UniverseView(self)

        log = self.query_one(Log)
        log.clear()
        log.write_line(" 123456789")
        log.write_line("1         1")
        log.write_line("2   █     2")
        log.write_line("3         3")
        log.write_line("4         4")
        log.write_line("5         5")
        log.write_line(" 123456789")

    def action_produce_next_generation(self) -> None:
        log = self.query_one(Log)
        log.clear()
        log.write_line(" 123456789")
        log.write_line("1         1")
        log.write_line("2         2")
        log.write_line("3         3")
        log.write_line("4         4")
        log.write_line("5         5")
        log.write_line(" 123456789")

    def action_reset_to_seed(self) -> None:
        log = self.query_one(Log)
        log.clear()
        log.write_line(" 123456789")
        log.write_line("1         1")
        log.write_line("2   █     2")
        log.write_line("3         3")
        log.write_line("4         4")
        log.write_line("5         5")
        log.write_line(" 123456789")

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = GameApp()
    app.run()
