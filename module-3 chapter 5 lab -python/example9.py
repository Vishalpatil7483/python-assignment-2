# 9. Count the Occurrences of Each Character
print("Name: Rakshitha P \nReg no: 23BTIT145")
def character_count(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    return counts

# Example usage
input_string = "hello"
print(character_count(input_string))  
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
