# apart from arithmetic operators, Python also provides several other types of operators
# these operators can be categorized into the following types:
# 1. Arithmetic Operators
# 2. Comparison Operators
# 3. Logical Operators
# 4. Assignment Operators
# 5. Bitwise Operators
# 6. Membership Operators
# 7. Identity Operators
# Let's discuss each type of operator with examples
# 1. Arithmetic Operators: These operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.
a = 10
b = 3
print(a + b)    # Addition: Output: 13
print(a - b)    # Subtraction: Output: 7
print(a * b)    # Multiplication: Output: 30
print(a / b)    # Division: Output: 3.3333333333333335
print(a % b)    # Modulus: Output: 1
print(a ** b)   # Exponentiation: Output: 1000
print(a // b)   # Floor Division: Output: 3
# 2. Comparison Operators: These operators are used to compare two values and return a boolean result (True or False)
print(a == b)   # Equal to: Output: False
print(a != b)   # Not equal to: Output: True
print(a > b)    # Greater than: Output: True
print(a < b)    # Less than: Output: False
print(a >= b)   # Greater than or equal to: Output: True
print(a <= b)   # Less than or equal to: Output: False
# 3. Logical Operators: These operators are used to combine multiple boolean expressions
x = True
y = False
print(x and y)  # Logical AND: Output: False
print(x or y)   # Logical OR: Output: True
print(not x)    # Logical NOT: Output: False
# 4. Assignment Operators: These operators are used to assign values to variables
c = 5
c += 2      # Equivalent to c = c + 2
print(c)    # Output: 7
c -= 3      # Equivalent to c = c - 3
print(c)    # Output: 4
c *= 4      # Equivalent to c = c * 4
print(c)    # Output: 16
c /= 2      # Equivalent to c = c / 2
print(c)    # Output: 8.0
c %= 3      # Equivalent to c = c % 3
print(c)    # Output: 2.0
# 5. Bitwise Operators: These operators are used to perform bit-level operations on integers
p = 5      # Binary: 0101
q = 3      # Binary: 0011
print(p & q)   # Bitwise AND: Output: 1 (Binary: 0001)
print(p | q)   # Bitwise OR: Output: 7 (Binary: 0111)
print(p ^ q)   # Bitwise XOR: Output: 6 (Binary: 0110)
print(~p)      # Bitwise NOT: Output: -6 (Binary: ...11111010)
print(p << 1)  # Bitwise Left Shift: Output: 10 (Binary: 1010)
print(p >> 1)  # Bitwise Right Shift: Output: 2 (Binary: 0010)
# 6. Membership Operators: These operators are used to check if a value is present in a sequence (like a list, tuple, or string)
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)      # Output: True     
print(6 not in my_list)  # Output: True
# 7. Identity Operators: These operators are used to compare the memory locations of two objects
a = [1, 2, 3]   
b = a
c = [1, 2, 3]
print(a is b)      # Output: True (a and b refer to the same object)
print(a is c)      # Output: False (a and c refer to different objects) 
print(a is not c)  # Output: True
# This is a basic overview of operators in Python.
 