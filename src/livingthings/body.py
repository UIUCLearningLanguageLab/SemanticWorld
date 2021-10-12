class Body:

	def __init__(self, phenotype):

		self.physical_property_label_list = []
		self.physical_property_index_dict = {}
		self.physical_property_dict = {}
		self.num_physical_properties = 0

		self.state_label_list = []
		self.state_index_dict = {}
		self.state_dict = {}
		self.num_states = 0
		self.state_category_dict = {}

		self.composition_dict = {}
		self.composition_label_list = []
		self.composition_index_dict = {}
		self.num_composites = 0

		self.metabolism_dict = {}
		self.metabolism_label_list = []
		self.metabolism_index_dict = {}
		self.num_metabolizables = 0

		self.initialize_physical_properties(phenotype.trait_dict['physical'])
		self.initialize_body_states(phenotype.trait_dict['body_states'])
		self.initialize_body_composition(phenotype.trait_dict['body_composition'])
		self.initialize_metabolism(phenotype.trait_dict['metabolism'])
		
	def initialize_physical_properties(self, physical_trait_dict):
		for physical_trait in physical_trait_dict:
			data = physical_trait.split('-')
			physical_trait_label = data[0]
			self.physical_property_label_list.append(physical_trait_label)
			self.physical_property_index_dict[physical_trait_label] = self.num_physical_properties
			self.num_physical_properties += 1
			self.physical_property_dict[physical_trait_label] = physical_trait_dict[physical_trait]

	def initialize_body_states(self, body_states_dict):
		for state in body_states_dict:
			data = state.split('-')
			state_label = data[0]
			category = data[1]
			self.state_category_dict[state_label] = category
			self.state_label_list.append(state_label)
			self.state_index_dict[state_label] = self.num_states
			self.num_states += 1
			self.state_dict[state_label] = body_states_dict[state]
	
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

