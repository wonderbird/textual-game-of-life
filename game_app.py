from textual.app import App, ComposeResult
from textual.widgets import Log, Footer, Header
from cell import Cell


class UniverseView:
    def __init__(self, app: App) -> None:
        self._app = app
        self._log = self._app.query_one(Log)
        self._cells = []
        self._presenter = UniversePresenter(self)

    def on_produce_next_generation(self) -> None:
        self._presenter.go_to_next_generation()

    def update(self) -> None:
        lines = [
            " 012345678",
            "0         0",
            "1         1",
            "2         2",
            "3         3",
            "4         4",
            " 012345678",
        ]

        for cell in self._cells:
            column = cell.get_x() + 1
            row = cell.get_y() + 1
            affected_line = lines[row]
            left = affected_line[:column]
            right = affected_line[column + 1 :]
            lines[row] = left + "█" + right

        self._log.clear()
        for line in lines:
            self._log.write_line(line)

    def add(self, x: int, y: int) -> None:
        self._cells.append(Cell(x, y))

    def remove(self, x: int, y: int) -> None:
        self._cells = []

    def clear(self) -> None:
        self._cells = []


class UniversePresenter:
    # introduce the universe model and move the universe construction from game app to the model
    # then the universe model can read the universe from the file universe.toml
    # https://docs.python.org/3/library/tomllib.html#module-tomllib
    # https://toml.io/en/v1.0.0#array
    def __init__(self, view: UniverseView) -> None:
        self._view = view
        self._model = []

    def reset_to_seed(self) -> None:
        self._model = []

        # Single cell is expected to die in the next generation
        self._model.append(Cell(1, 3))

        # Cluster of cells with 1 neighbor is expected to die in the next generation
        self._model.append(Cell(3, 1))
        self._model.append(Cell(4, 1))

        # Cluster with 2 neighbors for each cell is expected to live in the next generation
        # self._model.append(Cell(7, 2))
        # self._model.append(Cell(7, 3))
        # self._model.append(Cell(6, 3))

        self._view.clear()
        for cell in self._model:
            self._view.add(cell.get_x(), cell.get_y())

        self._view.update()

    def go_to_next_generation(self) -> None:
        self._view.remove(3, 1)
        self._view.update()


class GameApp(App):
    CSS_PATH = "style.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("n", "produce_next_generation", "Next generation"),
        ("r", "reset_to_seed", "Reset to seed"),
    ]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._universe_view = None

    def compose(self) -> ComposeResult:
        yield Header()
        yield Log(id="universe")
        yield Footer()

    def on_mount(self) -> None:
        self.log("We can send log messages to the textual console now.")

    def on_ready(self) -> None:
        self._universe_view = UniverseView(self)
        self.action_reset_to_seed()

    def action_produce_next_generation(self) -> None:
        self._universe_view.on_produce_next_generation()

    def action_reset_to_seed(self) -> None:
        self._universe_view.clear()

        # Single cell is expected to die in the next generation
        self._universe_view.add(1, 3)

        # Cluster of cells with 1 neighbor is expected to die in the next generation
        self._universe_view.add(3, 1)
        self._universe_view.add(4, 1)

        # Cluster with 2 neighbors for each cell is expected to live in the next generation
        # self._universe_view.add(7, 2)
        # self._universe_view.add(7, 3)
        # self._universe_view.add(6, 3)

        self._universe_view.update()

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = GameApp()
    app.run()
