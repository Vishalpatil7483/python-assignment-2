# 2.3 Practical Example 
# Here’s a complete example demonstrating the usage of os.path:
print("Name: Rakshitha P \nReg no: 23BTIT145")
import os

# Create a path
file_name = 'example.txt'
directory = 'Documents'
full_path = os.path.join(directory, file_name)

# Check if the file exists
if os.path.exists(full_path):
    print(f"{full_path} exists.")
else:
    print(f"{full_path} does not exist.")