# 10. Remove Whitespace from a String
print("Name: Rakshitha P \nReg no: 23BTIT145")
def remove_whitespace(s):
    return ''.join(s.split())

# Example usage
input_string = " Hello, World! "
print(remove_whitespace(input_string))  # Output: "Hello,World!"