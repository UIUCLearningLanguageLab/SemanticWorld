class Body:

	def __init__(self, phenotype):

		self.position_label_list = []
		self.position_index_dict = {}
		self.position_dict = {}
		self.num_positions = 0
		self.position_category_dict = {}

		self.composition_dict = {}
		self.composition_label_list = []
		self.composition_index_dict = {}
		self.num_composites = 0

		self.metabolism_dict = {}
		self.metabolism_label_list = []
		self.metabolism_index_dict = {}
		self.num_metabolizables = 0

		body_state_counter = 0
		while 'body_states' + str(body_state_counter) in phenotype.trait_dict:
			self.initialize_body_states(body_state_counter, phenotype.trait_dict['body_states' + str(body_state_counter)])
			body_state_counter += 1
		print(body_state_counter)

		self.initialize_body_composition(phenotype.trait_dict['body_composition'])
		self.initialize_metabolism(phenotype.trait_dict['metabolism'])

	def initialize_body_states(self, category, body_position_dict):
		for position in body_position_dict:
			self.position_category_dict[position] = category
			self.position_label_list.append(position)
			self.position_index_dict[position] = self.num_positions
			self.num_positions += 1
			self.position_dict[position] = body_position_dict[position]
	
	def initialize_body_composition(self, body_composition_dict):
		for composite in body_composition_dict:
			data = composite.split('-')
			composite_label = data[0]
			self.composition_label_list.append(composite_label)
			self.composition_index_dict[composite_label] = self.num_composites
			self.composition_dict[composite_label] = body_composition_dict[composite]
			self.num_composites += 1
	
	def initialize_metabolism(self, metabolism_dict):
		for metabolizable in metabolism_dict:
			data = metabolizable.split('-')
			metabolizable_label = data[0]
			self.metabolism_label_list.append(metabolizable_label)
			self.metabolism_index_dict[metabolizable_label] = self.num_metabolizables
			self.metabolism_dict[metabolizable] = metabolism_dict[metabolizable]
			self.num_metabolizables += 1

