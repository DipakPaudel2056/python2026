# we will discuss conditionals in Python
# Conditionals in Python
# Conditionals are used to perform different actions based on different conditions.
# The most common conditional statements in Python are if, elif, and else.
# if statement
x = 10
if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5
# if-else statement
y = 3
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")              # Output: y is odd
# if-elif-else statement
z = 0
if z > 0:
    print("z is positive")
elif z < 0:
    print("z is negative")
else:
    print("z is zero")             # Output: z is zero
# Nested if statement
a = 15
if a > 10:
    if a < 20:
        print("a is between 10 and 20")  # Output: a is between 10 and 20
# You can also use logical operators (and, or, not) with conditionals
b = 8
if b > 5 and b < 10:
    print("b is between 5 and 10")      # Output: b is between 5 and 10
if b < 5 or b > 10:
    print("b is either less than 5 or greater than 10")
else:
    print("b is between 5 and 10")      # Output: b is between 5 and 10
if not (b < 0):
    print("b is not negative")          # Output: b is not negative
# This is a basic overview of conditionals in Python.

# same as switch in js we have match case in python
day = 3
match day:
    case 1: 
        print("Monday")
    case 2: 
        print("Tuesday")
    case 3:
        print("Wednesday")  # Output: Wednesday
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")
# This is a basic overview of match-case statements in Python.