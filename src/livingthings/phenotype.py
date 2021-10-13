import numpy as np

class Phenotype:

	def __init__(self, genome):
		self.trait_dict = {'sex': {},
						   'appearance': {},
						   'physical': {},
						   'mental': {},
						   'body_states': {},
						   'body_composition': {},
						   'metabolism': {},
						   'drive_system': {},
						   'sensory_system': {},
						   'actions': {},}
			   
		self.appearance_dict = {}

		for gene_label in genome.gene_dict:
			gene = genome.gene_dict[gene_label]

			if gene.system in self.trait_dict:
				if gene.gene_type == 'summed_int':
					self.trait_dict[gene.system][gene_label] = self.calculate_summed_int_value(gene.sequence)
				elif gene.gene_type == 'binary_int':
					self.trait_dict[gene.system][gene_label] = self.calculate_binary_int_value(gene.sequence)
				elif gene.gene_type == 'summed_proportion':
					self.trait_dict[gene.system][gene_label] = self.calculate_summed_proportion_value(gene.sequence)
				elif gene.gene_type == 'binary_proportion':
					self.trait_dict[gene.system][gene_label] = self.calculate_binary_proportion_value(gene.sequence)
				else:
					raise Exception("Unrecognized gene type {} for gene {}".format(gene.gene_type, gene_label))

				if gene.visible:
					self.appearance_dict[gene_label] = self.trait_dict[gene.system][gene_label]
			
			else:
				raise Exception("Unrecognized system {} for gene {}".format(gene.system, gene_label))

	def __repr__(self):
		output_string = "Phenotype: {} traits\n".format(len(self.trait_dict))
		for system in self.trait_dict:
			output_string += "\n    {}\n".format(system)
			for trait_label in self.trait_dict[system]:
				if self.trait_dict[system][trait_label] < 1:
					value = "{:0.3f}".format(self.trait_dict[system][trait_label])
				else:
					value = self.trait_dict[system][trait_label]
				output_string += "        {}: {}\n".format(trait_label, value)
		return output_string

	def calculate_summed_int_value(self, gene_sequence):
		return sum(gene_sequence)

	def calculate_binary_int_value(self, gene_sequence):
		the_sum = 0
		counter = 0
		for i in range(len(gene_sequence)-1, -1, -1):
			the_sum += 2**counter * gene_sequence[i]
			counter += 1
		return the_sum

	def calculate_summed_proportion_value(self, gene_sequence):
		return sum(gene_sequence)/len(gene_sequence)

	def calculate_binary_proportion_value(self, gene_sequence):
		the_sum = 0
		counter = 0
		for i in range(len(gene_sequence)-1, -1, -1):
			the_sum += 2**counter * gene_sequence[i]
			counter += 1
		return the_sum / (2**len(gene_sequence)-1)