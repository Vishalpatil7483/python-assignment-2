# Example 6: Deleting a Directory 
print("Name: Rakshitha P \nReg no: 23BTIT145")
import shutil
import os

# Create a directory to delete
os.makedirs('directory_to_delete', exist_ok=True)

with open(os.path.join('directory_to_delete', 'temp_file.txt'), 'w') as f:
    f.write('This file will be deleted along with the directory.')

# Delete the directory and its contents
shutil.rmtree('directory_to_delete')

print('Directory "directory_to_delete" and all its contents were deleted.')