from textual.app import App, ComposeResult
from textual.widgets import Log, Footer, Header


class GameApp(App):
    CSS_PATH = "style.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("n", "produce_next_generation", "Next generation"),
        ("r", "reset_to_seed", "Reset to seed"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Log(id="universe")
        yield Footer()

    def on_ready(self) -> None:
        log = self.query_one(Log)
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
