# to create a class in python we use the keyword class followed by the class name and a colon.
class Dog:
    # constructor method to initialize the object
    def __init__(self, name, age):
        self.name = name  # instance variable for dog's name
        self.age = age    # instance variable for dog's age

    # method to make the dog bark
    def bark(self):
        return f"{self.name} says Woof!"

    # method to get the dog's age
    def get_age(self):
        return f"{self.name} is {self.age} years old."  
    
# Example usage
my_dog = Dog("Buddy", 3)
print(my_dog.bark())          # Output: Buddy says Woof!
print(my_dog.get_age())      # Output: Buddy is 3 years old.



# Inheritance example
class Puppy(Dog):
    def __init__(self, name, age, training_level):
        super().__init__(name, age)  # call the constructor of the parent class
        self.training_level = training_level  # additional instance variable for puppy

    # method to get the puppy's training level
    def get_training_level(self):
        return f"{self.name} is at {self.training_level} training level."
# Example usage
my_puppy = Puppy("Max", 1, "Beginner")
print(my_puppy.bark())                     # Output: Max says Woof!
print(my_puppy.get_age())                  # Output: Max is 1 years old.    
print(my_puppy.get_training_level())      # Output: Max is at Beginner training level.

# Encapsulation example
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder  # public instance variable
        self.__balance = balance               # private instance variable

    # method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance is {self.__balance}."
        else:
            return "Deposit amount must be positive."

    # method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. New balance is {self.__balance}."
        else:
            return "Insufficient funds or invalid withdrawal amount."

    # method to get the current balance
    def get_balance(self):
        return f"Current balance is {self.__balance}."
# Example usage
account = BankAccount("Alice", 1000)
print(account.deposit(500))          # Output: Deposited 500. New balance is 1500.
print(account.withdraw(200))         # Output: Withdrew 200. New balance is 1300.
print(account.get_balance())         # Output: Current balance is 1300.     

# Polymorphism example