import numpy as np

class DriveSystem:

	def __init__(self, drive_dict):
		self.num_drives = 0
		self.drive_label_list = []
		self.drive_index_dict = {}
		self.drive_array = None

		self.init_drive_system(drive_dict)
	
	def __repr__(self):
		output_string = "\nDrive System: {} drives\n".format(self.num_drives)
		for i in range(self.num_drives):
			output_string += "    {}) {}: {:0.3f}\n".format(i, self.drive_label_list[i], self.drive_array[i])
		return output_string

	def init_drive_system(self, drive_dict):
		self.drive_array = np.zeros([len(drive_dict)])

		for drive in drive_dict:
			self.drive_label_list.append(drive)
			self.drive_index_dict[drive] = self.num_drives
			self.num_drives += 1
	
	def update(self):
		pass


