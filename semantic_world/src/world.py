from .entities import entity
import random

class World:

    def __init__(self, world_params, entity_params):
        self.world_params = world_params
        self.entity_params = entity_params
        self.time_steps = world_params.time_steps
        self.dimensions = None
        self.num_entities = None
        self.entity_list = None

        self.create_world()

    def generate_position(self):
        x = random.randint(0, self.dimensions[0])
        y = random.randint(0, self.dimensions[1])
        return (x, y)

    def create_world(self):
        self.dimensions = self.world_params.dimensions
        self.num_entities = self.world_params.num_entities
        self.entity_list = []
        for i in range(self.num_entities):
            new_entity = entity.Entity(self.entity_params, i)
            self.entity_list.append(new_entity)
            new_entity.place_entity(self.generate_position())

    def run(self):
        for i in range(self.time_steps):
            self.update()
            print(self.entity_list[0])

    def update(self):
        for the_entity in self.entity_list:
            the_entity.update()

    def __str__(self):
        output_string = ("World:\n"
                         f"\tDimensions{self.dimensions}")
        return output_string