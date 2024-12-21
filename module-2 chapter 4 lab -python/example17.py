#Example 17. Flatten a Nested List
print("Name: Rakshitha P \nReg no: 23BTIT145")
nested_list = [[1, 2], [3, 4], [5]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)
