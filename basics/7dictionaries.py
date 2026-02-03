# dictionaries are ordered, changeable, and do not allow duplicates
# Dictionaries in Python
# A dictionary in Python is a collection of key-value pairs.
# Dictionaries are defined by enclosing elements in curly braces {} and separating them with commas.
# Here are some examples of creating and using dictionaries in Python:
# Creating a dictionary 
my_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
print(my_dict)            # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
# Accessing values in a dictionary
print(my_dict['name'])    # Output: John
print(my_dict.get('age')) # Output: 30
# Modifying values in a dictionary
my_dict['age'] = 31
print(my_dict)            # Output: {'name': 'John', 'age': 31, 'city': 'New York'}
# Adding key-value pairs to a dictionary
my_dict['job'] = 'Engineer'
print(my_dict)            # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'job': 'Engineer'}
# Removing key-value pairs from a dictionary
del my_dict['city']
print(my_dict)            # Output: {'name': 'John', 'age': 31, 'job': 'Engineer'}
popped_value = my_dict.pop('age')
print(popped_value)       # Output: 31
print(my_dict)            # Output: {'name': 'John', 'job': 'Engineer'}
# Looping through a dictionary  
for key, value in my_dict.items():
    print(f"{key}: {value}")    
# Output:
# name: John
# job: Engineer 
# Checking if a key exists in a dictionary
if 'name' in my_dict:
    print("Key 'name' found in dictionary") 
# Output: Key 'name' found in dictionary
else:
    print("Key 'name' not found in dictionary")
# Dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)       # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# This is a basic overview of dictionaries in Python.
# Dictionaries can also contain nested dictionaries
nested_dict = {
    'person1': {'name': 'Alice', 'age': 25},
    'person2': {'name': 'Bob', 'age': 30}
}
print(nested_dict)        # Output: {'person1': {'name': 'Alice', 'age': 25}, 'person2': {'name': 'Bob', 'age': 30}}
print(nested_dict['person1']['name'])  # Output: Alice
# This concludes our discussion on dictionaries in Python.