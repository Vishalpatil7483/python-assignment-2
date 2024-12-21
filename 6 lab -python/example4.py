# 5.3 Practical Example 
# Here’s a sample that demonstrates formatted output: 
print("Name: Rakshitha P \nReg no: 23BTIT145")
students = [("Alice", 22), ("Bob", 25), ("Charlie", 20)]

with open('students.txt', 'w') as file:
    for student in students:
        file.write("Name: {}, Age: {}\n".format(student[0], student[1]))
        print("code exicuted successfully")