# Example 5: FizzBuzz 
# This classic programming exercise prints numbers from 1 to 100 but replaces multiples of 3 with "Fizz," multiples of 5 with "Buzz," and multiples of both with "FizzBuzz." 
# FizzBuzz 
print("Name: Rakshitha P \nReg no: 23BTIT145")
for i in range(1, 101):     
    if i % 3 == 0 and i % 5 == 0: 
        print("FizzBuzz")     
    elif i % 3 == 0:         
        print("Fizz")     
    elif i % 5 == 0:         
        print("Buzz")     
    else: 
        print(i) 
