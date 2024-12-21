#Example 3. Count Occurrences
print("Name: Rakshitha P \nReg no: 23BTIT145")
fruits = ["apple", "banana", "apple", "orange", "banana"]
fruit_count = {fruit: fruits.count(fruit) for fruit in set(fruits)}
print(fruit_count)
