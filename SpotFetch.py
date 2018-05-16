import Src2TempFol as SF
import Temp2Fols as TF
import os

# stg_folder='N:\Projects\Anurag\Fol'
# phone_folder='N:\Projects\Anurag\Phone'
# laptop_folder='N:\Projects\Anurag\Laptop'

user_details=os.getlogin()
c_dir='C:\\Users'
main_dir=os.path.join(c_dir,user_details,'SpotFetch')
if not os.path.exists(main_dir):
    os.makedirs(main_dir)

Temp_Folder=os.path.join(main_dir,'Temp')
if not os.path.exists(Temp_Folder):
	os.makedirs(Temp_Folder)

Laptop_Folder=os.path.join(main_dir,'Laptop')
if not os.path.exists(Laptop_Folder):
	os.makedirs(Laptop_Folder)

Phone_Folder=os.path.join(main_dir,'Phone')
if not os.path.exists(Phone_Folder):
	os.makedirs(Phone_Folder)


a=SF.Src2TempFol(Temp_Folder)
a.copyFromSrc()


b=TF.Temp2Fols(Temp_Folder,Phone_Folder,Laptop_Folder)
b.filter2Fols()
