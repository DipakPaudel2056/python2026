# this is the new series where i will be teaching python from very basics to advance level
# in this file we will be discussing about data types in python
# Data types are the classification or categorization of data items.
# In Python, data types are used to define the type of a variable.
# Python has several built-in data types, including:
# 1. Numeric Types: int, float, complex
# 2. Sequence Types: list, tuple, range 
# 3. Text Type: str
# 4. Set Types: set, frozenset
# 5. Mapping Type: dict
# 6. Boolean Type: bool
# 7. Binary Types: bytes, bytearray, memoryview

# As we can see that the comments in the python file are written using the '#' symbol.
# anything written after the '#' symbol in a line is considered as a comment and is ignored by the python interpreter.

# Here are some examples of different data types in Python:
# Numeric Types
a = 10          # int
b = 10.5       # float  
c = 3 + 4j     # complex
# Sequence Types
my_list = [1, 2, 3, 4, 5]          # list
my_tuple = (1, 2, 3, 4, 5)         # tuple
my_range = range(1, 10)            # range
# Text Type
my_string = "Hello, World!"         # str
# Set Types
my_set = {1, 2, 3, 4, 5}            # set
my_frozenset = frozenset([1, 2, 3, 4, 5])  # frozenset
# Mapping Type
my_dict = {'name': 'John', 'age': 30}  # dict
# Boolean Type
is_true = True                      # bool
is_false = False                    # bool
# Binary Types
my_bytes = b'Hello'                 # bytes
my_bytearray = bytearray(5)        # bytearray
my_memoryview = memoryview(b'Hello')  # memoryview
# We can use the type() function to check the data type of a variable
print(type(a))              # <class 'int'>
print(type(b))              # <class 'float'>
print(type(c))              # <class 'complex'>
print(type(my_list))        # <class 'list'>
print(type(my_tuple))       # <class 'tuple'>
print(type(my_range))       # <class 'range'>
print(type(my_string))      # <class 'str'>
print(type(my_set))         # <class 'set'>
print(type(my_frozenset))   # <class 'frozenset'>
print(type(my_dict))        # <class 'dict'>
print(type(is_true))        # <class 'bool'>
print(type(is_false))       # <class 'bool'>
print(type(my_bytes))       # <class 'bytes'>
print(type(my_bytearray))   # <class 'bytearray'>
print(type(my_memoryview))  # <class 'memoryview'>
# This is a basic overview of data types in Python.
