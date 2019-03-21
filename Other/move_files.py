import re
import os
import shutil

os.chdir('C:/users/dx/desktop')
files = os.listdir('.')
folder = 'Moonman'
if not os.path.exists(folder):
    os.makedirs(folder)
for file in files:
    if re.match(folder,file):
        shutil.move(file,  folder)
        print(f'Moved {file} to {folder}')
