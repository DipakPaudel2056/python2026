# Lists in Python
# A list in Python is a collection of items that are ordered and changeable.
# Lists are defined by enclosing elements in square brackets [] and separating them with commas.
# Here are some examples of creating and using lists in Python:
# Creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list)            # Output: [1, 2, 3, 4, 5]
# Accessing elements in a list
print(my_list[0])         # Output: 1 (first element)
print(my_list[-1])        # Output: 5 (last element)
# Modifying elements in a list
my_list[2] = 10
print(my_list)            # Output: [1, 2, 10, 4, 5]
# Adding elements to a list
my_list.append(6)
print(my_list)            # Output: [1, 2, 10, 4, 5, 6]
my_list.insert(1, 15)
print(my_list)            # Output: [1, 15, 2, 10, 4, 5, 6]
# Removing elements from a list
my_list.remove(10)
print(my_list)            # Output: [1, 15, 2, 4, 5, 6]
popped_element = my_list.pop()
print(popped_element)      # Output: 6
print(my_list)            # Output: [1, 15, 2, 4, 5]
# List slicing  
sliced_list = my_list[1:4]
print(sliced_list)        # Output: [15, 2, 4]  
# Looping through a list
for item in my_list:
    print(item)
# Output:
# 1
# 15
# 2
# 4
# 5
# List comprehension
squared_list = [x**2 for x in my_list]
print(squared_list)       # Output: [1, 225, 4, 16, 25] 
# This is a basic overview of lists in Python.