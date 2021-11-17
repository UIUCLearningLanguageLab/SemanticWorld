import numpy as np
from config import world_cfg

class SensorySystem:

	def __init__(self, sensory_system_dict):

		self.visual_angle = sensory_system_dict['visual_angle']
		self.visual_field_range = sensory_system_dict['visual_field_range']
		self.visual_field_square_range = int(round(self.visual_field_range / world_cfg.World.tile_size))

		self.gets_entity_identity = sensory_system_dict['gets_entity_identity']
		self.gets_entity_coord = sensory_system_dict['gets_entity_coord']
		self.gets_entity_feature_labels = sensory_system_dict['gets_entity_feature_labels']
		self.gets_entity_feature_vector = sensory_system_dict['gets_entity_feature_vector']

		self.gets_terrain_coord = sensory_system_dict['gets_terrain_coord']
		self.gets_terrain_feature_labels = sensory_system_dict['gets_terrain_feature_labels']
		self.gets_terrain_feature_vector = sensory_system_dict['gets_terrain_feature_vector']

		self.sensation_list = []

	def get_visible_square_position_list(self, current_position):
		visible_square_position_list = []
		for x_offset in range(-self.visual_field_square_range, self.visual_field_square_range):
			for y_offset in range(-self.visual_field_square_range, self.visual_field_square_range):
				if (abs(x_offset) + abs(y_offset)) <= self.visual_field_square_range:
					if 0 <= (current_position[0] + x_offset) <= world_cfg.World.world_size[0]:
						if 0 <= (current_position[1] + y_offset) <= world_cfg.World.world_size[1]:
							visible_square_position_list.append((current_position[0] + x_offset, current_position[1] + y_offset))
		return visible_square_position_list

	def update_sensory_input(self, name, living_thing_position, the_world):
		living_thing_position = (int(round(living_thing_position[0])), int(round(living_thing_position[1])))
		self.sensation_list = []
		visible_square_position_list = self.get_visible_square_position_list(living_thing_position)
		for position in visible_square_position_list:
			new_terrain_sensation = TerrainSensation(the_world.terrain_map.terrain_tile_list[position[0]][position[1]], 
													 self.gets_terrain_coord, 
													 self.gets_terrain_feature_labels, 
													 self.gets_terrain_feature_vector)
			self.sensation_list.append(new_terrain_sensation)

			entity_list = the_world.terrain_map.terrain_tile_list[position[0]][position[1]].entity_list
			if len(entity_list) > 0:
				for entity in entity_list:
					if entity.name != name:
						new_entity_sensation = EntitySensation(entity, 
															self.gets_entity_identity,
															self.gets_entity_coord,
															self.gets_entity_feature_labels,
															self.gets_entity_feature_vector)
						self.sensation_list.append(new_entity_sensation)


class Sensation:

	def __init__(self, sensation_type=None):
		self.sensation_type = sensation_type
		self.position = None
		self.feature_label_list = None
		self.feature_vector = None

	def __repr__(self):
		output_string = "        {} Sensation   Position:{}\n".format(self.sensation_type, self.position)
		output_string += "           Features:{}\n".format(self.feature_label_list)
		output_string += "           Values:  {}\n".format(self.feature_vector)
		return output_string

class TerrainSensation(Sensation):

	def __init__(self, terrain_tile, gets_coord, gets_feature_labels, gets_feature_vector):
		super().__init__("terrain")
		if gets_coord:
			self.position = terrain_tile.position
		if gets_feature_labels:
			self.feature_label_list = terrain_tile.feature_label_list
		if gets_feature_vector:
			self.feature_vector = terrain_tile.feature_vector

class EntitySensation(Sensation):
	def __init__(self, entity, gets_identity, gets_coord, gets_feature_labels, gets_feature_vector):

		if gets_identity:
			super().__init__(entity.entity_type_label)
		else:
			super().__init__("entity")
		
		if gets_coord:
			self.position = entity.position
		if gets_feature_labels:
			self.feature_label_list = entity.appearance_feature_label_list
		if gets_feature_vector:
			self.feature_vector = entity.appearance_vector