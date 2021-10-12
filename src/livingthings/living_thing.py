from src import entities
from src.livingthings import genome, phenotype, body, drive_system, sensory_system, motor_system
from src.ai import ai
from copy import deepcopy


class LivingThing(entities.Entity):

	def __init__(self, entity_type_label, name, mother_genome=None, father_genome=None):
		super().__init__(entity_type_label)

		self.name = entity_type_label+str(name)
		self.age = 0
		self.genome = genome.Genome(entity_type_label, mother_genome, father_genome)
		self.phenotype = phenotype.Phenotype(deepcopy(self.genome))
		self.body = body.Body(deepcopy(self.phenotype))
		self.drive_system = drive_system.DriveSystem(deepcopy(self.phenotype.trait_dict['drive_system']))
		self.sensory_system = sensory_system.SensorySystem(deepcopy(self.phenotype.trait_dict['sensory_system']))

		self.update_appearance(self.phenotype.appearance_dict)

	#    self.motor_system = motor_system.MotorSystem(self.phenotype)
	#    self.ai = ai.AI()

	def take_turn(self, the_world):
		print("    {}".format(self.name))
		self.sensory_system.update_sensory_input(self.name, self.position, the_world)
		for sensation in self.sensory_system.sensation_list:
			print(sensation)
	#     action_choice_array = self.ai.choose_action(deepcopy(self.phenotype.trait_dict), deepcopy(self.phenotype.trait_index_dict),
	#                                                 deepcopy(self.body.body_state_array), deepcopy(self.body.body_state_index_dict),
	#                                                 deepcopy(self.drive_system.drive_state_array), deepcopy(self.drive_system.drive_state_index_dict),
	#                                                 deepcopy(self.sensory_system.sensory_array_list), deepcopy(self.sensory_system.sensory_index_dict),
	#                                                 deepcopy(self.motor_system.action_index_dict))
	#     self.motor_system.take_action(action_choice_array)
	#     self.update_living_thing()
	
	def update_living_thing(self):
	    self.age += 1
	    self.drive_system.update()

	

