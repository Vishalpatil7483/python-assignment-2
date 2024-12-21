# Program 2: Count Vowels in a String
print("Name: Rakshitha P \nReg no: 23BTIT145")
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

# Example usage
input_string = "Hello, World!"
print(count_vowels(input_string))