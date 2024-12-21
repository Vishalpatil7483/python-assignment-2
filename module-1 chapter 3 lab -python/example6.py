#Example 6.	Local vs. Global Scope 
print("Name: Rakshitha P \nReg no: 23BTIT145")
x = 10 
# Global variable 
def update_x():   
      global x 
      x += 5 
update_x()
print(x)  # Output: 15 