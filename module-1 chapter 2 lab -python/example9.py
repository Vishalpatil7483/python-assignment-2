# Example 9: Rock, Paper, Scissors Game 
# This program allows the user to play a simple game of Rock, Paper, Scissors against the computer.
print("Name: Rakshitha P \nReg no: 23BTIT145")
import random

# Define possible choices
choices = ["rock", "paper", "scissors"]

# Computer randomly selects a choice
computer_choice = random.choice(choices)

# Get user's choice and ensure it's in lowercase
user_choice = input("Enter rock, paper, or scissors: ").lower()

# Check if user's choice is valid
if user_choice not in choices:
    print("Invalid choice!")
else:
    print("Computer chose:", computer_choice)
    
    # Determine the outcome
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")
