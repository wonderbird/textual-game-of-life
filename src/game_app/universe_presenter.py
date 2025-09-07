from game_app.cell import Cell
from game_app.universe_view import UniverseView


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
            self._view.add(cell)

        self._view.update()

    def go_to_next_generation(self) -> None:
        self._view.remove(Cell(3, 1))
        self._view.update()
