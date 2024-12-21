#Example 4. Function Returning Multiple Values 
print("Name: Rakshitha P \nReg no: 23BTIT145")
def get_user_info():   
      name = "Alice"     
      age = 30     
      return name, age 
user_name, user_age = get_user_info() 
print(f"Name: {user_name}, Age: {user_age}")  
# Output: Name: Alice, Age: 30 
