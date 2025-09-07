import tomllib

from game_app.cell import Cell


class Universe:
    def __init__(self) -> None:
        self._universe_seed = []
        configuration_file = "universe.toml"

        with open(configuration_file, "rb") as f:
            data = tomllib.load(f)

        living_cells_x_y = data.get("living_cells_x_y")

        self._living_cells = []
        for x_y in living_cells_x_y:
            self._universe_seed.append(Cell(x_y[0], x_y[1]))

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
        self._living_cells = self._universe_seed.copy()

    def get_living_cells(self):
        return self._living_cells

    def go_to_next_generation(self):
        self._living_cells = []
