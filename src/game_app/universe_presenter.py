import tomllib

from game_app.cell import Cell
from game_app.universe_view import UniverseView


class UniversePresenter:
    def __init__(self, view: UniverseView) -> None:
        self._view = view
        self._model = []

    def reset_to_seed(self) -> None:
        # Read the universe from a "universe.toml" in the current directory
        # https://docs.python.org/3/library/tomllib.html#module-tomllib
        # https://toml.io/en/v1.0.0#array

        configuration_file = "universe.toml"

        with open(configuration_file, "rb") as f:
            data = tomllib.load(f)

        alive_cells_x_y = data.get("alive_cells_x_y")

        self._model = []
        for x_y in alive_cells_x_y:
            self._model.append(Cell(x_y[0], x_y[1]))

        # Cluster with 2 neighbors for each cell is expected to live in the next generation
        # self._model.append(Cell(7, 2))
        # self._model.append(Cell(7, 3))
        # self._model.append(Cell(6, 3))

        self._view.clear()
        for cell in self._model:
            self._view.add(cell)

        self._view.update()

    def go_to_next_generation(self) -> None:
        self._view.remove(Cell(3, 1))
        self._view.update()
