#Example 19. Remove Duplicates from List
print("Name: Rakshitha P \nReg no: 23BTIT145")
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(unique_numbers)

