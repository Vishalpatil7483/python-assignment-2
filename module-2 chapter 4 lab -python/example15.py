#Example 15. Nested Dictionary Access
print("Name: Rakshitha P \nReg no: 23BTIT145")
data = {
    "person": {
        "name": "John",
        "details": {
            "age": 30,
            "city": "New York"
        }
    }
}
print(data["person"]["details"]["city"])  # Output: New York