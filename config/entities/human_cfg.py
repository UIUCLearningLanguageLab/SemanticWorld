class Genome:
    ''' 
        genomes are defined over six variables:
        gene_label: the name of the gene, and the key in the dictionary below
        system:     the system for which the gene is relevant (general, drive system, sensory system, etc.)
        gene type:  whether the gene_sequence is used to generate a:
                        binary: a single bit that can be True or False
                        summed_float: value between 0 and 1, defined as binary value of gene_sequence/max_value (gene sequence of that size 
                                        that is all 1's)
                        binary_float: value between 0 and 1, defined as sum(gene_sequence) / gene_size
                        summed_int: value from 0 to gene_size, defined as sum(gene_sequence)
                        binary_int: value from 0 to 2**gene_size, defined as binary conversion of gene_sequence (right to left)
        gene size:  the number of bits in the gene sequence. 
                    will effect how big an int can be, or the precision after the decimal (will be increments of 1/(gene_size+1))
        mean:       population mean for that gene of a randomly generated sample
        stdev:      population stdev for that gene of a randomly generated sample
        mutable:    whether the gene is allowed to evolve
        visible:    whether the trait contributes to the entity's appearance vector

        traits are divided into categories, described below:
    '''

    traits = {
    # appearance traits affect how the living thing looks and its physical shape
        'sex':                  ['physical',     'binary_int',         1,       .5,           5,       True,      True], # male or female TODO make this more complex
        'head_volume':          ['physical',    'binary_int',         6,       50,           2,       True,      True],   # cubic cm
        'head_elipticality':    ['physical',    'binary_proportion',  8,       .5,          .05,      True,      True],   # 0 = perfectly round, 1 = maximally elliptical
        'torso_length':         ['physical',  'binary_int',         6,       47,           5,       True,      True],   # cm
        'shoulder_width':       ['physical',  'binary_int',         6,       38,           2,       True,      True],   # cm
        'chest_width':          ['physical',  'binary_int',         7,       106,          3,       True,      True],   # cm
        'waist_width':          ['physical',  'binary_int',         7,       92,           5,       True,      True],   # cm
        'hip_width':            ['physical',  'binary_int',         7,       98,           2,       True,      True],   # cm
        'leg_length':           ['physical',  'binary_int',         7,       85,           2,       True,      True],   # cm
        'leg_width':            ['physical',  'summed_proportion',  10,      .5,           2,       True,      True],    # cm
        'arm_length':           ['physical',  'binary_int',         5,       25,           1.5,     True,      True],   # cm
        'arm_width':            ['physical',  'summed_proportion',  10,      .5,           .15,     True,      True],    # cm
        'skin_color':           ['physical',  'summed_proportion',  20,      .5,           2,       True,      True],   # proportion of [45,34,30] to [255,195,170] in rgb
        'eye_color_red':        ['physical',  'binary_int',         8,       128,          2,       True,      True],   # r in rgb, proportion of 255
        'eye_color_green':      ['physical',  'binary_int',         8,       128,          2,       True,      True],   # g in rgb, proportion of 255
        'eye_color_blue':       ['physical',  'binary_int',         8,       128,          2,       True,      True],   # b in rgb, proportion of 255
        'hair_color_red':       ['physical',    'binary_int',         8,       128,          2,       True,      True],   # r in rgb, proportion of 255
        'hair_color_green':     ['physical',  'binary_int',         8,       128,          2,       True,      True],   # g in rgb, proportion of 255
        'hair_color_blue':      ['physical',  'binary_int',         8,       128,          2,       True,      True],   # b in rgb, proportion of 255
        'hair_curl':            ['physical',  'summed_proportion',  10,      .5,           5,       True,      True],   # proportion of straight (0) to circular curl (1)
        'hair_top_length':      ['physical',  'binary_int',         8,       10,           4,       True,      True],   # cm
        'hair_side_length':     ['physical',  'binary_int',         9,       100,          30,      True,      True],   # mm


    # personality traits that affect how the agent behaves)
        'openness':                 ['mental', 'summed_proportion', 10,        .5,         .2,      True,      False],
        'conscientiousness':        ['mental', 'summed_proportion', 10,        .5,         .2,      True,      False],
        'extraversion':             ['mental', 'summed_proportion', 10,        .5,         .2,      True,      False],
        'agreeableness':            ['mental', 'summed_proportion', 10,        .5,         .2,      True,      False],
        'neuroticism':              ['mental', 'summed_proportion', 10,        .5,         .2,      True,      False],


    # the body positions this entity can have, which may be used as conditions for actions
    # if the state is listed here at all, it will be an option for the living thing. The gene value specifies the initial value of the states
    # each body state is labeled name-category, where the category specifies a group of mutually exclusive body states. categories can be numbers or strings
        'standing-0':                 ['body_states', 'binary_int', 1, 1, 0, False, True],
        'sitting-0':                  ['body_states', 'binary_int', 1, 0, 0, False, True],
        'laying-0':                   ['body_states', 'binary_int', 1, 0, 0, False, True],
        'crouching-0':                ['body_states', 'binary_int', 1, 0, 0, False, True],
        'holding_left-1':             ['body_states', 'binary_int', 1, 0, 0, False, True],
        'holding_right-2':            ['body_states', 'binary_int', 1, 0, 0, False, True],

    # body composition affects how much energy the entity consumes
        'skin_composition':   ['body_composition', 'binary_int',  3,    6,      0,  False,  True],
        'muscle_composition': ['body_composition', 'summed_int',  20,   14,     2,  True,   True],
        'bone_composition':   ['body_composition', 'binary_int',  7,    6,      0,  False,  True],
        'fat_composition':    ['body_composition', 'summed_int',  20,   7,      1,  True,   True],
        'sugar_composition':  ['body_composition', 'binary_int',  7,    0.01,   0,  False,  True], 
        'starch_composition': ['body_composition', 'binary_int',  7,    0.00,   0,  False,  True],
        'fiber_composition':  ['body_composition', 'binary_int',  7,    0.00,   0,  False,  True],
        'water_composition':  ['body_composition', 'binary_int',  7,    0.64,   0,  False,  True],

    # metabolism affects what proportion of the energy the entity retains when eating something of the following compositions
        'skin_metabolism':    ['metabolism', 'binary_proportion',  7, 0.10, 0, False, False],
        'muscle_metabolism':  ['metabolism', 'binary_proportion',  7, 0.50, 0, False, False],
        'bone_metabolism':    ['metabolism', 'binary_proportion',  7, 0.01, 0, False, False],
        'fat_metabolism':     ['metabolism', 'binary_proportion',  7, 0.50, 0, False, False],
        'sugar_metabolism':   ['metabolism', 'binary_proportion',  7, 1.00, 0, False, False],
        'starch_metabolism':  ['metabolism', 'binary_proportion',  7, 1.00, 0, False, False],
        'fiber_metabolism':   ['metabolism', 'binary_proportion',  7, 0.00, 0, False, False],

    # drive states to populate which drives the entity will have, and the gene specifies a float value tied to that gene that the AI
    # can use for decision-making (for example, a threshold to use to decide to act based on that drive)
        'hunger':       ['drive_system', 'summed_proportion',  10, .5, .2, True, False],
        'thirst':       ['drive_system', 'summed_proportion',  10, .5, .2, True, False], 
        'sleepiness':   ['drive_system', 'summed_proportion',  10, .5, .2, True, False], 
        'fatigue':      ['drive_system', 'summed_proportion',  10, .5, .2, True, False],
        'pain':         ['drive_system', 'summed_proportion',  10, .5, .2, True, True],
 
     # sensory sysstem traits affecting what an entity can sense from it's environment
        'visual_angle':               ['sensory_system', 'binary_int',  9, 360, 0, False, False],  # the size of the visual peripheral field (in degrees)
        'visual_field_range':         ['sensory_system', 'binary_int',  6, 60, 0, False, False],   # the range of visual perception (in meters)
        'gets_entity_identity':       ['sensory_system', 'binary_int',  1, 1, 0, False, False],    # if true, entity receives a list of entity types for each entity in visual field
        'gets_entity_coord':          ['sensory_system', 'binary_int',  1, 1, 0, False, False],    # if true, entity receives a list of coordinates for each entity in visual field
        'gets_entity_feature_labels': ['sensory_system', 'binary_int',  1, 1, 0, False, False],    # if true, entity recieves a list of labels for entity feature vectors                                
        'gets_entity_feature_vector': ['sensory_system', 'binary_int',  1, 1, 0, False, False],    # if true, entity recieves a feature vector for each entity, in visual field
        'gets_terrain_coord':          ['sensory_system', 'binary_int',  1, 1, 0, False, False],   # if true, entity receives a list of coordinates for each terrain square in visual field
        'gets_terrain_feature_labels': ['sensory_system', 'binary_int',  1, 1, 0, False, False],   # if true, entity recieves a list of labels for terrain feature vectors                                
        'gets_terrain_feature_vector': ['sensory_system', 'binary_int',  1, 1, 0, False, False],   # if true, entity recieves a feature vector for each entity, in visual field           

        # motor system traits used to decide what actions an entity can take. Each action's list has an additional argument
        'sleep':             ['actions', 'binary_int',  1, 1, 0, False, True],
        'wake_up':           ['actions', 'binary_int',  1, 1, 0, False, True],
        'move':              ['actions', 'binary_int',  1, 1, 0, False, True],
        'rotate':            ['actions', 'binary_int',  1, 1, 0, False, True],
        'sit_down':          ['actions', 'binary_int',  1, 1, 0, False, True],
        'stand_up':          ['actions', 'binary_int',  1, 1, 0, False, True],
        'lay_down':          ['actions', 'binary_int',  1, 1, 0, False, True],
        'crouch':            ['actions', 'binary_int',  1, 1, 0, False, True],
        'grab_with_LH':      ['actions', 'binary_int',  1, 1, 0, False, True],
        'grab_with_RH':      ['actions', 'binary_int',  1, 1, 0, False, True],
        'drop_from_LF':      ['actions', 'binary_int',  1, 1, 0, False, True],
        'drop_from_RH':      ['actions', 'binary_int',  1, 1, 0, False, True],
        'eat_from_LH':       ['actions', 'binary_int',  1, 1, 0, False, True],
        'eat_from_RH':       ['actions', 'binary_int',  1, 1, 0, False, True],
        'drink_from_LH':     ['actions', 'binary_int',  1, 1, 0, False, True],
        'drink_from_RH':     ['actions', 'binary_int',  1, 1, 0, False, True],
    }
