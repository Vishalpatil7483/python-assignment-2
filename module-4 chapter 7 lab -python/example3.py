# Example 3: Moving a File 
print("Name: Rakshitha P \nReg no: 23BTIT145")
import shutil
import os

# Create a sample file to move
with open('file_to_move.txt', 'w') as f:
    f.write('This file will be moved.')

# Create the target directory if it doesn't exist
os.makedirs('destination_dir', exist_ok=True)

# Move the file
shutil.move('file_to_move.txt', 'destination_dir/file_to_move.txt')
print('File moved to "destination_dir/file_to_move.txt".')