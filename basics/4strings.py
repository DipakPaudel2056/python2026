# we already know how to create strings using single or double quotes
# in this file we will be discussing more about strings in python
# A string in Python is a sequence of characters enclosed within single quotes (' ') or double quotes (" ").
# Here are some examples of creating strings in Python:
str1 = 'Hello, World!'        # using single quotes
str2 = "Python is awesome!"    # using double quotes
print(str1)                    # Output: Hello, World!
print(str2)                    # Output: Python is awesome!
# You can also create multi-line strings using triple quotes (''' ''' or """ """).  
str3 = '''This is a
multi-line  string.'''
str4 = """You can also use                                                              
triple double quotes for multi-line strings."""
print(str3)
print(str4)
# Strings in Python are immutable, which means once a string is created, it cannot be changed.
# However, you can create a new string based on operations performed on the original string.
# Here are some common string operations in Python:
# Concatenation
greeting = str1 + " " + str2
print(greeting)                # Output: Hello, World! Python is awesome!
# Repetition
repeat_str = str1 * 3
print(repeat_str)              # Output: Hello, World!Hello, World!Hello, World!
# Slicing
sliced_str = str1[0:5]
print(sliced_str)              # Output: Hello
# Length
length = len(str2)
print(length)                  # Output: 18
# String Methods
upper_str = str2.upper()
print(upper_str)               # Output: PYTHON IS AWESOME!
lower_str = str2.lower()
print(lower_str)               # Output: python is awesome!
find_index = str1.find('World')
print(find_index)              # Output: 7
replace_str = str1.replace('World', 'Python')
print(replace_str)             # Output: Hello, Python!
# You can also use formatted strings (f-strings) to embed expressions inside string literals
name = "Alice"
age = 25
intro = f"My name is {name} and I am {age} years old."
print(intro)                   # Output: My name is Alice and I am 25 years old.
# This is a basic overview of strings in Python.
# in keyword is used to check if a substring exists within a string
substring = "Python"
if substring in str2:
    print(f"'{substring}' found in str2") 
# Output: 'Python' found in str2
else:
    print(f"'{substring}' not found in str2")
    # Output: 'Python' not found in str2
# You can also iterate through each character in a string using a for loop
for char in str1:
    print(char)
# This will print each character in str1 on a new line
# This concludes our discussion on strings in Python.