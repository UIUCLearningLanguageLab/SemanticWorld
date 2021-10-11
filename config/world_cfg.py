class World:

	# these control the random map generation
	world_size = (300, 400) 				# this is how many Map tiles are in the world
	

	
	land_size = (20,20)   				# (20,20) island will usually occupy half of screen, bigger means smaller island, more water
	height_range = (-10, 50)			# these will be the min and max height values, with everything scaled in between
	num_peaks = 2						# this is how many random peaks are summed together using a random 2D gaussian
	peak_position_range = (.25, .25)    # this is the proportion of world size (counting from middle x & y) where peaks can spawn
	peak_variance_range = (.1, .2)		# this is peak variance, in terms of the proportion of land size

	tile_size = 1						# this is the size of each tile, in "meters"

	# these are general properties of entities
	mutation_rate: 0.01
	
	# these control the size of each population and rules about their distribution
	living_things = {
				'human': {
							'n': 1,
							'distribution': ['random', 4],			# can be ['random'] or ['clustered', n], where n is variance from cluster center
							'config_file': 'human_cfg',
						 }
	}

	nonliving_things = {}

