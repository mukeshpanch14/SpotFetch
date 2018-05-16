# ########################################################################
# Src Folder to Temporary Folder
# Inputs- Temporary Folder Location
#         
# Developer- P PANCH MUKESH
# ########################################################################

import os
from shutil import copy

class Src2TempFol(object):
	def __init__(self,tgt_folder):
		self.tgt_folder=tgt_folder

	def copyFromSrc(self):

		user_details=os.getlogin()
		c_dir='C:\\Users'
		spot_location='AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'
		src_folder=os.path.join(c_dir,user_details,spot_location)
		#print(src_folder)

		#tgt_folder='N:\Projects\Anurag\Fol'
		for file in os.listdir(src_folder):
			os.chdir(src_folder)
			file_path=os.path.join(src_folder,file)
			newfile=file+'.jpg'
			tgt_file_path=os.path.join(self.tgt_folder,newfile)
			copy(file_path,tgt_file_path)


