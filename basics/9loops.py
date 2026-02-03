# python has 2 loop commands
# for loop
# while loop
# for loop
print("for loop example:")
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4
# looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple 
# banana
# cherry
# while loop
print("while loop example:")
count = 0
while count < 5:
    print(count)
    count += 1
# Output:
# 0
# 1
# 2
# 3
# 4
# using break in loops
print("break statement example:")
for i in range(10):
    if i == 5:
        break
    print(i)    
# Output:
# 0
# 1
# 2
# 3
# 4
# using continue in loops
print("continue statement example:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# Output:
# 1
# 3
# 5
# using else with loops
print("else statement with loop example:")
for i in range(5):
    print(i)
else:
    print("Loop completed")
# Output:
# 0
# 1
# 2
# 3
# 4
# Loop completed
# This is a basic overview of loops in Python.