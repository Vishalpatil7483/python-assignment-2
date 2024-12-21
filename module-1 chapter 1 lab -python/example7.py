# Example 7: List of Favorite Foods 
# This program collects a list of favorite foods from the user and displays them. 
# Favorite Foods List 
print("Name: vaishnav \nReg no: 23BTIT164")
foods = []
for _ in range(3): 
    food = input("Enter your favorite food: ")    
    foods.append(food)
    print("Your favorite foods are:", ", ".join(foods)) 
