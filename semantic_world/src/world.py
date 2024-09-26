

class World:

    def __init__(self, world_params):
            self.dimensions = world_params.dimensions

    def __str__(self):
        output_string = ("World:\n"
                         f"\tDimensions{self.dimensions}")
        return output_string