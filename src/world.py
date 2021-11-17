from config import world_cfg
import numpy as np
from src import terrain
from src.livingthings import living_thing
import random
import sys

class World:

	def __init__(self):

		self.living_thing_list = []
		self.nonliviing_thing_list = []

		self.living_thing_count_dict = {}
		self.nonliving_thing_count_dict = {}

		self.terrain_map = terrain.TerrainMap()
		self.turn_counter = 0

		self.place_living_things()
		print(self)

	def __repr__(self):
		output_string = "\nWorld:\n"
		output_string += "   Map Size: {}\n".format(self.terrain_map.shape)
		output_string += "   Living Things:\n"
		for label in self.living_thing_count_dict:
			output_string += "       {}: {}\n".format(label, self.living_thing_count_dict[label])
			for living_thing in self.living_thing_list:
				if living_thing.entity_type_label == label:
					output_string += "            {}: {}\n".format(living_thing.name, living_thing.position)
		return output_string

	def place_living_things(self):
		print("    Placing Living Things")
		for label in world_cfg.World.living_things:
			n = world_cfg.World.living_things[label]['n']
			distribution = world_cfg.World.living_things[label]['distribution']
			print("        Placing {} of type {}".format(n, label))
			cluster_center  = self.generate_random_position()
			for i in range(n):
				new_living_thing = living_thing.LivingThing(label, i, None, None)
				if distribution[0] == 'random':
					start_position = self.generate_random_position()
				elif distribution[0] == 'clustered':
					start_position = cluster_center
				else:
					raise Exception("Unrecognized rule {} for generating start position".format(distribution[0]))

				new_living_thing.position = start_position
				self.terrain_map.terrain_tile_list[start_position[0]][start_position[1]].entity_list.append(new_living_thing)
				self.living_thing_list.append(new_living_thing)

				if label not in self.living_thing_count_dict:
					self.living_thing_count_dict[label] = 0
				self.living_thing_count_dict[label] += 1
				
	def generate_random_position(self):
		legal_position = False
		n = 0
		while not legal_position:
			x = random.randint(0, self.terrain_map.shape[0]-1)
			y = random.randint(0, self.terrain_map.shape[1]-1)
			
			if self.terrain_map.terrain_tile_list[x][y].elevation > 0:
				legal_position = True
			n += 1
			if n > 1000:
				print("INFINITE LOOP")
				sys.exit()
		return np.array([x,y])
	
	def next(self):
		print("Starting Turn {}".format(self.turn_counter))
		for living_thing in self.living_thing_list:
			living_thing.take_turn(self)   # TODO figure out a way to make the reference to world passed in as read only
		self.turn_counter += 1
		



