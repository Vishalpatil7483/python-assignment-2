# Example 1: Copying a File 
print("Name: Rakshitha P \nReg no: 23BTIT145")
import shutil

# Create a sample file
with open('sample_file.txt', 'w') as f:
    f.write('This file will be copied.')

# Copy the file
shutil.copy('sample_file.txt', 'copied_file.txt')

print('File copied from "sample_file.txt" to "copied_file.txt"')