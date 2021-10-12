from config import world_cfg
import sys
import math
import random
import numpy as np
import matplotlib.pyplot as plt

class TerrainMap:

	def __init__(self):

		self.shape = (world_cfg.World.world_size[0], world_cfg.World.world_size[1])
		print("    Creating Terrain Map of Size", self.shape)
		self.elevation_matrix = None
		self.terrain_tile_list = None

		if self.shape[0] < 10 or self.shape[1] < 10:
			print("ERROR, World num_rows and num_cols must be at least 10.")
			sys.exit(1)

		self.create_elevation_map()
		self.create_terrain_tile_matrix()
	
	def create_elevation_map(self):
		
		x_size = world_cfg.World.land_size[0]
		y_size = world_cfg.World.land_size[1]

		mu_x_range = (round(x_size/2 - x_size*world_cfg.World.peak_position_range[0]), round(x_size/2 + x_size*world_cfg.World.peak_position_range[0]))
		mu_y_range = (round(y_size/2 - y_size*world_cfg.World.peak_position_range[1]), round(y_size/2 + y_size*world_cfg.World.peak_position_range[1]))
		sigma_x_range = (x_size*world_cfg.World.peak_variance_range[0], x_size*world_cfg.World.peak_variance_range[1])
		sigma_y_range = (y_size*world_cfg.World.peak_variance_range[0], y_size*world_cfg.World.peak_variance_range[1])

		self.elevation_matrix = np.zeros([world_cfg.World.world_size[0], world_cfg.World.world_size[1]], float)
		x_inc = x_size/world_cfg.World.world_size[0]
		y_inc = y_size/world_cfg.World.world_size[1]

		for i in range(world_cfg.World.num_peaks):
			mu_x = random.randint(mu_x_range[0], mu_x_range[1])
			mu_y = random.randint(mu_y_range[0], mu_y_range[1])
			sigma_x = random.uniform(sigma_x_range[0], sigma_x_range[1])
			sigma_y = random.uniform(sigma_y_range[0], sigma_y_range[1])

			for j in range(world_cfg.World.world_size[0]):
				x = j*x_inc
				for k in range(world_cfg.World.world_size[1]):
					y = k*y_inc
					self.elevation_matrix[j, k] += (1 / (2* math.pi * sigma_x * sigma_y) * math.e**(-((x-mu_x)**2/(2*sigma_x**2)+(y-mu_y)**2/(2*sigma_y**2))))
 
		the_max = self.elevation_matrix.max()
		the_min = self.elevation_matrix.min()
		max_elevation = world_cfg.World.height_range[1]
		min_elevation = world_cfg.World.height_range[0]
		conversion_slope = (max_elevation-min_elevation) / (the_max-the_min)
		conversion_intercept = min_elevation-conversion_slope*the_min
		self.elevation_matrix = conversion_slope*self.elevation_matrix + conversion_intercept
		#self.plot_elevation_matrix()

	def print_elevation_matrix(self):
		for i in range(self.elevation_matrix.shape[0]):
			output_string = str(i)
			for j in range(self.elevation_matrix.shape[1]):
				output_string += " {:0.3f}".format(self.elevation_matrix[i,j])
			print(output_string)
	
	def plot_elevation_matrix(self):
		c = plt.imshow(self.elevation_matrix, cmap='terrain')
		plt.colorbar(c)
		plt.show()


	def create_terrain_tile_matrix(self):
		self.terrain_tile_list = []
		for x in range(self.shape[0]):
			new_row_list = []
			for y in range(self.shape[1]):
				new_row_list.append(TerrainTile(x, y, self.elevation_matrix[x,y]))
			self.terrain_tile_list.append(new_row_list)

class TerrainTile:

	def __init__(self, x, y, elevation):
		self.position = (x, y)
		self.size = world_cfg.World.tile_size
		self.elevation = elevation
		self.entity_list = []

		self.num_features = 1
		self.feature_label_list = []
		self.feature_label_index_dict = {}
		self.feature_vector = np.zeros([self.num_features])

		self.init_features()
	
	def __repr__(self):
		output_string = "Terrain Tile: ({},{})   Elevation: {:0.2f}\n".format(self.position[0], self.position[1], self.elevation)
		return output_string

	def init_features(self):

		self.feature_label_list.append("elevation")
		self.feature_label_index_dict["elevation"] = 0
		self.feature_vector[0] = self.elevation