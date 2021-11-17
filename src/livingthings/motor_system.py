import importlib

class MotorSystem:

	def __init__(self, the_living_thing):

		self.the_living_thing = the_living_thing
		self.num_actions = 0
		self.action_label_list = []
		self.action_index_dict = {}
		self.action_result_dict = {}
		self.action_requirement_dict = {}

		self.load_action_primitives()

	def load_action_primitives(self):

		import config.entities.human.action_primitives as action_primitives
		# TODO replace the line above with something like the code below that uses species variable to load module automatically
		# rather than hard coding for human
		#entity_cfg_filename = "config.entities." + self.the_living_thing.entity_type_label + ".action_primitives.py"
		# try:
		# 	action_primitives_info_file = importlib.import_module(entity_cfg_filename)
		# except:
		# 	raise Exception("Could not load config file {}".format(entity_cfg_filename))

		self.action_primitives = action_primitives.ActionPrimitives()

		for action_primitive in self.action_primitives.action_primitive_dict:
			self.action_label_list.append(action_primitive)
			self.action_index_dict[action_primitive] = self.num_actions
			self.num_actions += 1
	
	def take_action(self, action_value_array):
		for i in range(len(action_value_array)):
			label = self.action_label_list[i]
			for action in self.action_primitives.action_primitive_dict[label]:
				action(action_value_array[i], self.the_living_thing)