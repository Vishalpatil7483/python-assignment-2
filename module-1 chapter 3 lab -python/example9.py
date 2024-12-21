#Example 9.	Factorial Function with Recursion
print("Name: Rakshitha P \nReg no: 23BTIT145")
def factorial(n): 
    if n == 0 or n == 1: 
        return 1     
    return n * factorial(n - 1) 
print(factorial(5))  # Output: 120