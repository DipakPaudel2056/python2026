# in the other file we have already discussed about data types in python
# now in this file we will be discussing about variables in python
# A variable in Python is a reserved memory location to store values.   
# In other words, a variable in a python program gives data to the computer for processing.
# Unlike some other programming languages, Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
# Here are some examples of how to create and use variables in Python:
# Creating variables
x = 5               # integer variable
y = 3.14            # float variable
name = "Alice"     # string variable
is_active = True    # boolean variable
# Using variables
print(x)            # Output: 5
print(y)            # Output: 3.14
print(name)         # Output: Alice
print(is_active)    # Output: True
# You can also change the value of a variable by assigning a new value to it
x = 10
print(x)            # Output: 10
# You can use variables in expressions
sum_value = x + y
print(sum_value)    # Output: 13.14
# You can also use the type() function to check the data type of a variable
print(type(x))      # Output: <class 'int'>
print(type(y))      # Output: <class 'float'>   
print(type(name))   # Output: <class 'str'>
print(type(is_active))  # Output: <class 'bool'>
# This is a basic overview of variables in Python.
# Variables in Python are dynamically typed, which means you don't need to declare their type explicitly.
# The interpreter infers the type based on the value assigned to the variable.
# You can also assign multiple variables in a single line
a, b, c = 1, 2.5, "Hello"
print(a)        # Output: 1
print(b)        # Output: 2.5
print(c)        # Output: Hello
# You can also assign the same value to multiple variables in a single line
m = n = p = 100
print(m)        # Output: 100
print(n)        # Output: 100
print(p)        # Output: 100
# This concludes our discussion on variables in Python.