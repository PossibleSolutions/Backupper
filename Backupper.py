import os
import shutil

# specify your source and destination directories
source_dir = r'CopyYourPath'
dest_dir = r'CopyYourPath'

# get a list of all python and ipynb files in the source directory
python_files = [f for f in os.listdir(source_dir) if f.endswith('.py') or f.endswith('.ipynb')]
print(len(python_files))

# copy each file to the destination directory
for file in python_files:
    shutil.copy(os.path.join(source_dir, file), dest_dir)