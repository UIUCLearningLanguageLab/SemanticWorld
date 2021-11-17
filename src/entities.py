import numpy as np

class Entity:
	
	def __init__(self, entity_type_label):

		self.name = None
		self.entity_type_label = entity_type_label

		self.position = None
		self.size = None
		self.mass = None

		self.num_properties = 0
		self.property_label_list = []
		self.property_index_dict = {}
		self.property_dict = {}

		self.appearance_size = 0
		self.appearance_dict = {}
		self.appearance_feature_label_list = []
		self.appearance_feature_label_index_dict = {}
		self.appearance_vector = None

	def update_appearance(self, appearance_dict):
		self.appearance_dict = appearance_dict
		self.appearance_vector = np.zeros([len(appearance_dict)])
		for label in appearance_dict:
			self.appearance_feature_label_list.append(label)
			self.appearance_feature_label_index_dict[label] = self.appearance_size
			self.appearance_vector[self.appearance_size] = appearance_dict[label]
			self.appearance_size += 1

