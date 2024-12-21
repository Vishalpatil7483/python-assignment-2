# Section 4: Saving Variables with the shelve Module 
# 4.2 Saving Data 
# Here’s how to use the shelve module: 
print("Name: Vishal \nReg no: 23BTIT167")
import shelve

# Saving data
with shelve.open('mydata') as db:
    db['key1'] = [1, 2, 3]
    db['key2'] = {'name': 'Alice', 'age': 30}
# 4.3 Retrieving Data 
# To retrieve the data, you can simply access the keys: 
with shelve.open('mydata') as db:
    print(db['key1'])  # Output: [1, 2, 3]
    print(db['key2'])  # Output: {'name': 'Alice', 'age': 30}