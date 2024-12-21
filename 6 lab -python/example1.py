# 1.3 Practical Example 
# To open a file using both absolute and relative paths in Python: 
# Using an absolute path
print("Name: Rakshitha P \nReg no: 23BTIT145")
absolute_path = r'C:\Users\vp988\Documents\example.txt'

with open(absolute_path, 'r') as file:
    content = file.read()
    print(content)

# Using a relative path
relative_path = 'Documents/example.txt'

with open(relative_path, 'r') as file:
    content = file.read()
    print(content)