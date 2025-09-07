import tomllib


class UniverseReader:
    def read(self) -> list[list[int]]:
        configuration_file = "universe.toml"

        with open(configuration_file, "rb") as f:
            data = tomllib.load(f)

        return data.get("living_cells_x_y")
