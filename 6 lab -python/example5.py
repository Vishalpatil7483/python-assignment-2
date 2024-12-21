# Section 6: Project: Generating Random Quiz Files 
print("Name: Rakshitha P \nReg no: 23BTIT145")
import random
questions = [
    ("What is the capital of France?", "Paris"),
    ("What is 2 + 2?", "4"),
    ("What is the color of the sky?", "Blue"),
]

random.shuffle(questions)

with open('quiz.txt', 'w') as file:
    for question, answer in questions:
        file.write(f"{question} (Answer: {answer})\n")

print("instructions witten into quiz.txt succesfull")