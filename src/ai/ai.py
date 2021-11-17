import numpy as np
import random

class AI:

    def __init__(self, the_living_thing):

        self.num_actions = the_living_thing.motor_system.num_actions
        self.action_choice_array = None
        self.action_iterator = 0
        

    def choose_action(self, the_living_thing):
        self.action_choice_array = np.zeros([self.num_actions], float)
        self.action_choice_array[self.action_iterator] = random.choice([-1,1])
        self.action_iterator += 1
        if self.action_iterator == self.num_actions:
            self.action_iterator = 0

        return self.action_choice_array