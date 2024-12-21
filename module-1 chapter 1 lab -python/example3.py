# Example 3: Simple Interest Calculator 
# This program calculates simple interest based on user input. 
# Simple Interest Calculator 
print("Name: vaishnav \nReg no: 23BTIT164")

principal = float(input("Enter principal amount: ")) 
rate = float(input("Enter rate of interest (in %): "))
time = float(input("Enter time (in years): ")) 
simple_interest = (principal * rate * time) / 100
print("The simple interest is:", simple_interest) 
