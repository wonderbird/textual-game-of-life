import tomllib

from game_app.cell import Cell


class UniverseReader:
    def read(self) -> list[Cell]:
        """Read "universe.toml" in the current directory.

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

        living_cells_xy = data.get("living_cells_x_y")

        result = []
        for x_y in living_cells_xy:
            x = x_y[0]
            y = x_y[1]
            result.append(Cell(x, y))

        return result
