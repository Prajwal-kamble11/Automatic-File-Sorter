import os
import shutil
path = input("Enter your path: ")
files=os.listdir(path)
print(files)

for file in files:
    filename , extension = os.path.splitext(file)
    extension = extension[1: ]
    print(extension)
    
    if extension == "":
        continue
    
    folder_path = os.path.join(path,extension)
    
    if os.path.exists( folder_path):
        shutil.move(os.path.join(path,file) , os.path.join( folder_path,file))
    else: 
        os.makedirs(folder_path)
        shutil.move(os.path.join(path,file) , folder_path,file)
print("Process Ended.")