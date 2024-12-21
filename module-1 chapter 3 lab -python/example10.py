#Example 10. Finding Maximum Value in a List 
print("Name: Rakshitha P \nReg no: 23BTIT145")
def find_max(numbers):    
    max_value = numbers[0]  
    for num in numbers:     
        if num > max_value:        
            max_value = num     
    return max_value 
 
numbers = [3, 1, 4, 1, 5, 9, 2]
print(find_max(numbers))  # Output: 9 
