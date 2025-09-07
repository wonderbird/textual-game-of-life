import tomllib

from game_app.cell import Cell


class Universe:
    def __init__(self) -> None:
        self._alive_cells = []
        self.reset()

    def reset(self):
        configuration_file = "universe.toml"

        with open(configuration_file, "rb") as f:
            data = tomllib.load(f)

        alive_cells_x_y = data.get("alive_cells_x_y")

        self._alive_cells = []
        for x_y in alive_cells_x_y:
            self._alive_cells.append(Cell(x_y[0], x_y[1]))

    def get_alive_cells(self):
        return self._alive_cells
