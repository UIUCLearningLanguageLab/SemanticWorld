import random
import numpy as np


class Entity:

    def __init__(self, entity_params, entity_number):

        self.entity_params = entity_params
        self.entity_number = entity_number
        self.dimensions = None
        self.color = None
        self.position = None
        self.orientation = None
        self.orientation_options = [np.array([0, -1]),
                                    np.array([0, 1]),
                                    np.array([1, 0]),
                                    np.array([-1, 0])]

        self.speed = self.entity_params.speed

        self.create_entity()

    def __str__(self):
        output_string = (f"Entity {self.entity_number}:\n"
                         f"\tDimensions: {self.dimensions}\n"
                         f"\tColor: {self.color}\n"
                         f"\tPosition: {self.position}\n\n")
        return output_string

    def create_entity(self):
        self.dimensions = (self.entity_params.dimensions[0], self.entity_params.dimensions[1])
        self.color = random.choice(self.entity_params.color_options)
        self.orientation = random.choice(self.orientation_options)

    def place_entity(self, position):
        self.position = position

    def rotate(self):
        self.orientation = random.choice(self.orientation_options)

    def move(self):
        self.position += self.speed * self.orientation

    def update(self):
        self.rotate()
        self.move()