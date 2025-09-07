import tomllib

from game_app.cell import Cell
from game_app.universe import Universe
from game_app.universe_view import UniverseView


class UniversePresenter:
    def __init__(self, view: UniverseView) -> None:
        self._view = view
        self._model = []
        self._universe = Universe()

    def reset_to_seed(self) -> None:
        self._universe.reset()
        self._model = self._universe.get_alive_cells()

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
