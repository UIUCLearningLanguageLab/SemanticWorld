import math
import numpy as np

class ActionPrimitives:
        # the set of action primitives. Each action must:
        #       be added to the primitive dict with the name of the primitive as a key, and a list of functions that are called as the value
        #       have the functions associated with it defined below. these functions must 
        #               return a list of changes that will be made to the living thing. 
        #                       this is a list of tuples, containing the name of a property and the new value of the property
        #                       these properties must refer to either global properties of the living thing (like position or direction)

        #   a list of requirements, conditions that must be true for the action to be legal
        #   a list of results, changes to the living thing that occur if the action is taken.
        #   the value of each primitive will be a number between -1 and 1, and can be used as an argument


        def __init__(self):
                
                # every action must be defined in terms of checks against or changes to properties of the living thing
                # those can be univeral properties (like position, facing, mass, ), 
                # or they can be species-specific properties (like "standing" for "human")

                self.action_primitive_dict = {
                        'move':         [self.move],
                        'rotate':       [self.rotate],
                        'stand_up':     [self.stand_up],
                        'sit_down':     [self.sit_down],
                        'sit_up':       [self.sit_up],
                        'lay_down':     [self.lay_down],
                        'pick_up_left': [self.pick_up_left],
                        'pick_up_right': [self.pick_up_right],
                }

        def move(self, value, the_living_thing):
                if the_living_thing.phenotype.trait_dict["body_states0"]["standing"]:
                        radians_heading = math.radians(the_living_thing.heading)
                        position_delta = np.array([math.cos(radians_heading), math.sin(radians_heading)])
                        max_speed = the_living_thing.phenotype.trait_dict['physical']['max_speed']
                        the_living_thing.position = the_living_thing.position + max_speed*value*position_delta

        def rotate(self, value, the_living_thing):
                if the_living_thing.phenotype.trait_dict["body_states0"]["standing"]:
                        the_living_thing.heading += value*180
        
        def stand_up(self, value, the_living_thing):
                if value == 1:
                        if the_living_thing.phenotype.trait_dict["body_states0"]["sitting"]:
                                the_living_thing.phenotype.trait_dict["body_states0"]["standing"] = 1
                                the_living_thing.phenotype.trait_dict["body_states0"]["sitting"] = 0

        def sit_down(self, value, the_living_thing):
                if value == 1:
                        if the_living_thing.phenotype.trait_dict["body_states0"]["standing"]:
                                the_living_thing.phenotype.trait_dict["body_states0"]["sitting"] = 1
                                the_living_thing.phenotype.trait_dict["body_states0"]["standing"] = 0

        def sit_up(self, value, the_living_thing):
                if value == 1:
                        if the_living_thing.phenotype.trait_dict["body_states0"]["laying"]:
                                the_living_thing.phenotype.trait_dict["body_states0"]["sitting"] = 1
                                the_living_thing.phenotype.trait_dict["body_states0"]["laying"] = 0

        def lay_down(self, value, the_living_thing):
                if value == 1:
                        if the_living_thing.phenotype.trait_dict["body_states0"]["sitting"]:
                                the_living_thing.phenotype.trait_dict["body_states0"]["laying"] = 1
                                the_living_thing.phenotype.trait_dict["body_states0"]["sitting"] = 0

        def reach_left_x(self, value, the_living_thing):
                pass

        def reach_left_y(self, value, the_living_thing):
                pass

        def reach_left_z(self, value, the_living_thing):
                pass
        
        def pick_up_left(self, value, the_living_thing):
                if value == 1:
                        # if there is an entity in the same position as your hand
                                # if that entity's mass < max_strength
                                the_living_thing.phenotype.trait_dict["body_states1"]["holding_left"] = 1

        def pick_up_right(self, value, the_living_thing):
                if value == 1:
                        # if there is an entity in the same position as your hand
                                # if that entity's mass < max_strength
                                the_living_thing.phenotype.trait_dict["body_states2"]["holding_right"] = 1

        def eat_with_left(self, value, the_living_thing):
                if value == 1:
                        if the_living_thing.phenotype.trait_dict["body_states1"]["holding_with_left"] == 1:
                                the_living_thing.metabolize()                

        def eat_with_left(self, value, the_living_thing):
                if value == 1:
                        if the_living_thing.phenotype.trait_dict["body_states1"]["holding_with_left"] == 1:
                                the_living_thing.metabolize()  
