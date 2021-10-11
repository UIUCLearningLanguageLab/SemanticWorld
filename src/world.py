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

		self.terrain_map = terrain.TerrainMap()

		self.place_entities()

		# for living_thing in self.living_thing_list:
		# 	print(living_thing, living_thing.position)
		# print()
		# for i in range(self.terrain_map.shape[0]):
		# 	for j in range(self.terrain_map.shape[1]):
		# 		if len(self.terrain_map.terrain_tile_list[i][j].entity_list) > 0:
		# 			print(i, j, self.terrain_map.terrain_tile_list[i][j].position,
		# 			self.terrain_map.terrain_tile_list[i][j].elevation, self.terrain_map.terrain_tile_list[i][j].entity_list)
	
	def place_entities(self):
		print("    Placing Entities")
		for label in world_cfg.World.living_things:
			n = world_cfg.World.living_things[label]['n']
			distribution = world_cfg.World.living_things[label]['distribution']
			print("        Placing {} of type {}".format(n, label))
			cluster_center  = self.generate_random_position()
			for i in range(n):
				new_living_thing = living_thing.LivingThing(label, None, None)
				if distribution[0] == 'random':
					start_position = self.generate_random_position()
				elif distribution[0] == 'clustered':
					start_position = cluster_center
				else:
					raise Exception("Unrecognized rule {} for generating start position".format(distribution[0]))

				new_living_thing.position = start_position
				self.terrain_map.terrain_tile_list[start_position[0]][start_position[1]].entity_list.append(new_living_thing)
				self.living_thing_list.append(new_living_thing)
				
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
		return (x,y)
	
	def next(self):
		for animate_entity in self.animate_entity_list:
			animate_entity.take_turn()





