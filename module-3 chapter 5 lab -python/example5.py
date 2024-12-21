
# Program 5: Find the First Non-Repeating Character
print("Name: Rakshitha P \nReg no: 23BTIT145")
def first_non_repeating(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    for char in s:
        if counts[char] == 1:
            return char
    return None

# Example usage
input_string = "swiss"
print(first_non_repeating(input_string))
