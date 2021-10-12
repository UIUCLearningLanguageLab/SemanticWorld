import numpy as np

class DriveSystem:

	def __init__(self, drive_dict):
		self.num_drives = 0
		self.drive_label_list = []
		self.drive_index_dict = {}
		self.drive_array = None
	

	def init_drive_system(self, drive_dict):
		self.drive_array = np.zeros([len(drive_dict)])

		for drive in drive_dict:
			self.drive_label_list.append(drive)
			self.drive_index_dict[drive] = self.num_drives
			self.num_drives += 1


