import tomllib

from game_app.cell import Cell


class Universe:
    def __init__(self, universe_seed: list[Cell]) -> None:
        self._universe_seed = universe_seed.copy()
        self._living_cells = []
        self.reset()

    def reset(self):
        self._living_cells = self._universe_seed.copy()

    def get_living_cells(self):
        return self._living_cells

    def go_to_next_generation(self):
        self._living_cells = []
