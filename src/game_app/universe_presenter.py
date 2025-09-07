import tomllib

from game_app.cell import Cell
from game_app.universe_view import UniverseView


class UniversePresenter:
    def __init__(self, view: UniverseView) -> None:
        self._view = view
        self._model = []

    def reset_to_seed(self) -> None:
        # TODO: Next is to read the universe from a file named universe.toml
        # https://docs.python.org/3/library/tomllib.html#module-tomllib
        # https://toml.io/en/v1.0.0#array
        self._model = []

        toml_string = """
            alive_cells = [[1, 3], [3, 1], [4, 1]]
            """
        data = tomllib.loads(toml_string)

        cells_as_nested_list = data.get("alive_cells")
        for cell_coordinates in cells_as_nested_list:
            self._model.append(Cell(cell_coordinates[0], cell_coordinates[1]))

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
