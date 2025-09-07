from game_app.universe import Universe
from game_app.universe_reader import UniverseReader
from game_app.universe_view import UniverseView


class UniversePresenter:
    def __init__(self, view: UniverseView) -> None:
        self._view = view
        self._universe = Universe(UniverseReader().read())

    def reset_to_seed(self) -> None:
        self._universe.reset()

        self._view.clear()
        for cell in self._universe.get_living_cells():
            self._view.add(cell)

        self._view.update()

    def go_to_next_generation(self) -> None:
        currently_living_cells = set(self._universe.get_living_cells())

        self._universe.go_to_next_generation()

        next_living_cells = set(self._universe.get_living_cells())

        dying_cells = currently_living_cells - next_living_cells
        for cell in dying_cells:
            self._view.remove(cell)

        self._view.update()
