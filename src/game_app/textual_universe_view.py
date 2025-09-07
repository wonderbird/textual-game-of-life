from textual.app import App
from textual.widgets import Log

from game_app.cell import Cell
from game_app.universe_presenter import UniversePresenter
from game_app.universe_view import UniverseView


class TextualUniverseView(UniverseView):
    def __init__(self, app: App) -> None:
        self._app = app
        self._log = self._app.query_one(Log)
        self._cells = []
        self._presenter = UniversePresenter(self)

    def on_produce_next_generation(self) -> None:
        self._presenter.go_to_next_generation()

    def on_reset_to_seed(self) -> None:
        self._presenter.reset_to_seed()

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

    def add(self, cell: Cell) -> None:
        self._cells.append(cell)

    def remove(self, cell: Cell) -> None:
        self._cells = []

    def clear(self) -> None:
        self._cells = []
