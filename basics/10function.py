# functions in Python
def greet(name):
    """This function greets the person passed in as a parameter"""
    return f"Hello, {name}!"
# Example usage
print(greet("Alice"))
# Output: Hello, Alice!
def add(a, b):
    """This function returns the sum of two numbers"""
    return a + b
# Example usage
print(add(5, 3))
# Output: 8
def factorial(n):
    """This function returns the factorial of a number"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 
# Example usage
print(factorial(5))
# Output: 120
# Lambda function example
square = lambda x: x * x
# Example usage
print(square(4))
# Output: 16
# Function with default parameter
def power(base, exponent=2):
    """This function returns the base raised to the exponent"""
    return base ** exponent
# Example usage
print(power(3))
# Output: 9
print(power(2, 3))
# Output: 8
# Function with variable number of arguments
def multiply(*args):
    """This function returns the product of all arguments"""
    result = 1
    for num in args:
        result *= num
    return result   
# Example usage
print(multiply(2, 3, 4))
# Output: 24
# Function with keyword arguments
def introduce(**kwargs):
    """This function introduces a person using keyword arguments"""
    introduction = ", ".join(f"{key}: {value}" for key, value in kwargs.items())
    return f"Introduction - {introduction}" 
# Example usage
print(introduce(name="Bob", age=30, city="New York"))
# Output: Introduction - name: Bob, age: 30, city: New York
# Nested function example
def outer_function(text):
    """This function contains a nested function"""
    def inner_function():
        return text.upper()
    return inner_function()
# Example usage
print(outer_function("hello"))
# Output: HELLO
# Function with docstring
def square_root(x):
    """This function returns the square root of a number"""
    return x ** 0.5
# Example usage
print(square_root(16))
# Output: 4.0
print(square_root.__doc__)
# Output: This function returns the square root of a number
# Function with type hints
def divide(a: float, b: float) -> float:
    """This function returns the division of two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
# Example usage
print(divide(10, 2))
# Output: 5.0
print(divide.__annotations__)
# Output: {'a': <class 'float'>, 'b': <class 'float'>, '
# return': <class 'float'>}
# Function with recursion
def fibonacci(n):
    """This function returns the nth Fibonacci number"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  
# Example usage
print(fibonacci(6))
# Output: 8
# Function with higher-order function
def apply_function(func, value):
    """This function applies a given function to a value"""
    return func(value)
# Example usage
print(apply_function(lambda x: x + 10, 5))
# Output: 15
print(apply_function(square, 7))
# Output: 49
# Function with closure
def make_multiplier(factor):
    """This function returns a multiplier function"""
    def multiplier(number):
        return number * factor
    return multiplier
# Example usage
double = make_multiplier(2)
print(double(5))
# Output: 10
triple = make_multiplier(3)
print(triple(5))
# Output: 15
# Function with exception handling
def safe_divide(a, b):
    """This function safely divides two numbers and handles division by zero"""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed" 
# Example usage
print(safe_divide(10, 2))
# Output: 5.0
print(safe_divide(10, 0))
# Output: Error: Division by zero is not allowed
# Function with map and filter
def square_even_numbers(numbers):
    """This function returns a list of squares of even numbers from the input list"""
    return list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, numbers)))    
# Example usage
print(square_even_numbers([1, 2, 3, 4, 5, 6]))
# Output: [4, 16, 36]   
# Function with list comprehension
def get_positive_numbers(numbers):
    """This function returns a list of positive numbers from the input list"""
    return [num for num in numbers if num > 0]  
# Example usage
print(get_positive_numbers([-10, 5, -3, 2, 0, 8]))
# Output: [5, 2, 8] 

# decorator example
def my_decorator(func):
    """This is a simple decorator that prints a message before and after the function call"""
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper
@my_decorator
def say_hello(name):
    """This function says hello to the given name"""
    print(f"Hello, {name}!")    
# Example usage
say_hello("Charlie")
# Output:
# Before the function call  
# Hello, Charlie!
# After the function call
print(say_hello.__doc__)
# Output: This function says hello to the given name
print(say_hello.__name__)
# Output: say_hello
print(my_decorator.__doc__)
# Output: This is a simple decorator that prints a message before and after the function call
def timer_decorator(func):
    """This decorator measures the execution time of a function"""
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper
@timer_decorator
def compute_sum(n):
    """This function computes the sum of numbers from 1 to n"""
    return sum(range(1, n + 1))
# Example usage
print(compute_sum(1000000))
# Output: Execution time: <time_in_seconds> seconds
# 500000500000
print(compute_sum.__doc__)
# Output: This function computes the sum of numbers from 1 to n
print(compute_sum.__name__)
# Output: compute_sum
print(timer_decorator.__doc__)
# Output: This decorator measures the execution time of a function


# generator function example
def fibonacci_generator(n):
    """This generator function yields the first n Fibonacci numbers"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
# Example usage
for num in fibonacci_generator(10):
    print(num, end=" ")
# Output: 0 1 1 2 3 5 8 13 21 34
