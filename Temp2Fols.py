# ########################################################################
# Temporary Folder to Two folders 1.Laptop 2.Phone
# Inputs- Temporary Folder Location
#         Phone Folder
#         Laptop Folder
# Developer- P PANCH MUKESH
# ########################################################################

from PIL import Image
import os
from shutil import copy
class Temp2Fols(object):
    def __init__(self,stg_folder,phone_folder,laptop_folder):
        self.stg_folder=stg_folder
        self.phone_folder=phone_folder
        self.laptop_folder=laptop_folder

# stg_folder='N:\Projects\Anurag\Fol'
# phone_folder='N:\Projects\Anurag\Phone'
# laptop_folder='N:\Projects\Anurag\Laptop'
    def filter2Fols(self):
        for file in os.listdir(self.stg_folder):
            if file.endswith('.jpg'):
                os.chdir(self.stg_folder)
                with Image.open(file) as img:
                    width, height=img.size
                file_path=os.path.join(self.stg_folder,file)
                # print(file_path)
                # print(width,height)


                if width==1920 and height==1080:
                    new_file_path=os.path.join(self.laptop_folder,file)
                    copy(file_path,self.laptop_folder+os.path.join('/',file))
                elif width==1080 and height==1920:
                    new_file_path=os.path.join(self.phone_folder,file)
                    copy(file_path,self.phone_folder+os.path.join('/',file))