#Example 7. Exception Handling  Example
print("Name: Rakshitha P \nReg no: 23BTIT145")
def safe_divide(a, b): 
    try: 
        return a / b   
    except ZeroDivisionError: 
        return "Cannot divide by zero!" 
print(safe_divide(10, 2))  # Output: 5.0 
print(safe_divide(10, 0))  # Output: Cannot divide by zero! 
