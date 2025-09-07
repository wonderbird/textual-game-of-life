import tomllib

from game_app.cell import Cell


class Universe:
    def __init__(self) -> None:
        self._living_cells = []
        self.reset()

    def reset(self):
        """Initialize by reading "universe.toml" in the current directory.

        Replaces the internal state by the living cells specified in the file.

        Example file:

        ```toml
        living_cells_x_y = [[1, 3], [2, 3]]
        ```

        Documentation for parsing TOML:

        - https://docs.python.org/3/library/tomllib.html#module-tomllib
        - https://toml.io/en/v1.0.0#array
        """
        configuration_file = "universe.toml"

        with open(configuration_file, "rb") as f:
            data = tomllib.load(f)

        living_cells_x_y = data.get("living_cells_x_y")

        self._living_cells = []
        for x_y in living_cells_x_y:
            self._living_cells.append(Cell(x_y[0], x_y[1]))

    def get_alive_cells(self):
        return self._living_cells
