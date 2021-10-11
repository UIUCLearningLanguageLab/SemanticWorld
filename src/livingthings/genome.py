from config import world_cfg
import random
import sys
import numpy as np
from copy import deepcopy
import importlib

class Genome:

	def __init__(self, species, mother_genome, father_genome):

		self.species = species
		self.num_genes = 0
		self.gene_label_list = []
		self.gene_index_dict = {}
		self.gene_dict = {}
		
		self.mother_genome = mother_genome
		self.father_genome = father_genome

		if mother_genome == None or father_genome == None:
			self.generate_genome(self.species)
		else:
			self.inheret_genome(self.mother_genome, self.father_genome)

	def inheret_genome(self, mother_genome, father_genome):
		success = True
		if mother_genome.num_genes == father_genome.num_genes:
			self.num_genes = mother_genome.num_genes
			self.gene_label_list = deepcopy(mother_genome.gene_label_list)
			self.gene_dict = deepcopy(mother_genome.gene_dict)
			self.gene_index_dict = deepcopy(mother_genome.gene_index_dict)
			
			for i in range(self.num_genes):
				if mother_genome.gene_label_list == father_genome.gene_label_list:
					father_gene = father_genome.gene_dict[self.gene_label_list[i]]
					self.gene_dict[self.gene_label_list[i]] = self.gene_dict[self.gene_label_list[i]].reproduction(father_gene)
				else:
					print("Inheret Genome failed because parents' gene " + str(i) + " did not match")
					success = False
			for i in range(self.num_constants):
				if mother_genome.constant_label_list == father_genome.constant_label_list:
					mother_constant = mother_genome.constant_dict[self.constant_label_list[i]]
					father_constant = father_genome.constant_dict[self.constant_label_list[i]]
					self.constant_dict[self.constant_label_list[i]] = random.choice([mother_constant, father_constant])
				else:
					print("Inheret Genome failed because parents' constant " + str(i) + " did not match")	
					success = False
		else:
			print("Inheret Genome failed because parents' num_genes or num_constants were not same size")
			success = False
		return success


	def generate_genome(self, species):
		self.num_genes = 0
		self.gene_dict = {}
		self.gene_index_dict = {}
		self.gene_label_list = []

		species_cfg_filename = "config.entities." + species + "_cfg"
		try:
			genome_info = importlib.import_module(species_cfg_filename)
		except:
			raise Exception("Could not load config file {}".format(species_cfg_filename))
		
		for trait_label in genome_info.Genome.traits:
			# TODO error checking on cfg files

			new_gene = Gene()
			new_gene.generate_gene(trait_label,
								   genome_info.Genome.traits[trait_label][0],
								   genome_info.Genome.traits[trait_label][1],
								   genome_info.Genome.traits[trait_label][2],
								   genome_info.Genome.traits[trait_label][3],
								   genome_info.Genome.traits[trait_label][4],
								   genome_info.Genome.traits[trait_label][5],
								   genome_info.Genome.traits[trait_label][6],
			)
			self.gene_label_list.append(trait_label)
			self.gene_index_dict[trait_label] = self.num_genes
			self.num_genes += 1
			self.gene_dict[trait_label] = new_gene

class Gene:

	def __init__(self):
		self.label = None
		self.system = None
		self.gene_type = None
		self.gene_size = None
		self.pop_mean = None
		self.pop_stdev = None
		self.mutable = None
		self.visible = None
		self.sequence = None
		self.mutation_rate = .01  # TODO put this in the config files somewhere and import
	
	def __repr__(self):
		output_string = "Gene: {}\n".format(self.label)
		output_string += "    System: {}    Type:{}   Size:{}   PopMean:{}   PopStdev:{}  Mutable:{}   Visible:{}\n".format(self.system,
																											 self.gene_type, 
																											 self.gene_size, 
																											 self.pop_mean,
																											 self.pop_stdev, 
																											 self.mutable, 
																											 self.visible)
		output_string += "    Sequence: {}\n".format(self.sequence)
		return output_string

	def reproduction(self, father_sequence):
		for i in range(self.gene_size):
			if father_sequence is not None:
				if random.randint(0,1) == 0:
					self.sequence[i] = father_sequence[i]
			if self.mutable:
				if random.random() < self.mutation_rate:
					self._sequence[i] = 1-self.sequence[i]

	def generate_gene(self, label, system, gene_type, gene_size, pop_mean, pop_stdev, mutable, visible):
		self.label = label
		self.system = system
		self.gene_type = gene_type
		self.gene_size = gene_size
		self.pop_mean = pop_mean
		self.pop_stdev = pop_stdev
		self.mutable = mutable
		self.visible = visible

		# TODO error check the trait dict in the cfg file, including making sure there are no duplicate keys

		if gene_type == 'binary_proportion':
			self.generate_binary_proportion_sequence()
		elif gene_type == 'summed_proportion':
			self.generate_summed_proportion_sequence()
		elif gene_type == 'binary_int':
			self.generate_binary_int_sequence()
		elif gene_type == 'summed_int':
			self.generate_summed_int_sequence()
		else:
			raise Exception("Unrecognized trait type for {}".format(label))

	def generate_binary_int_sequence(self):
		self.sequence = np.zeros([self.gene_size])
		random_trait_value = round(np.random.normal(self.pop_mean, self.pop_stdev))
		if random_trait_value < 0:
			trait_value = 0
		elif random_trait_value > (2**self.gene_size-1):
			trait_value = 2**self.gene_size-1
		else:
			trait_value = random_trait_value

		binary_string = format(trait_value, '0'+str(self.gene_size)+'b')

		if len(binary_string) > self.gene_size:
			raise Exception("Binary int {} representing {} too big for gene size {}".format(binary_string, trait_value, self.gene_size))
		else:
			for i in range(len(binary_string)):
				self.sequence[i] = int(binary_string[i])
	
	def generate_summed_int_sequence(self):
		self.sequence = np.zeros([self.gene_size])
		random_trait_value = round(np.random.normal(self.pop_mean, self.pop_stdev))
		if random_trait_value < 0:
			trait_value = 0
		elif random_trait_value > self.gene_size:
			trait_value = self.gene_size
		else:
			trait_value = random_trait_value

		index_list = list(range(self.gene_size))
		random.shuffle(index_list)
		for i in range(trait_value):
			index = index_list[i]
			self.sequence[index] = 1
	
	def generate_binary_proportion_sequence(self):
		self.sequence = np.zeros([self.gene_size])
		random_trait_value = np.random.normal(self.pop_mean, self.pop_stdev)
		possible_values = np.linspace(0,1,2**self.gene_size)
		index = (np.abs(possible_values - random_trait_value)).argmin()
		binary_string = format(index, '0'+str(self.gene_size)+'b')
		if len(binary_string) > self.gene_size:
			raise Exception("Binary string {} representing value {} too big for gene size {}".format(binary_string, possible_values[index], self.gene_size))
		else:
			for i in range(len(binary_string)):
				self.sequence[i] = int(binary_string[i])

	def generate_summed_proportion_sequence(self):
		self.sequence = np.zeros([self.gene_size])
		random_trait_value = np.random.normal(self.pop_mean, self.pop_stdev)
		possible_values = np.linspace(0, 1, self.gene_size+1)
		index = (np.abs(possible_values - random_trait_value)).argmin()

		index_list = list(range(self.gene_size))
		random.shuffle(index_list)
		for i in range(index):
			index = index_list[i]
			self.sequence[index] = 1