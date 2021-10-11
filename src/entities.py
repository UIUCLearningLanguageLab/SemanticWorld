class Entity:
	
	def __init__(self, entity_type_label):

		self.entity_type_label = entity_type_label

		self.position = None
		self.size = None
		self.mass = None

		self.num_properties = 0
		self.property_label_list = []
		self.property_index_dict = []
		self.property_dict = {}