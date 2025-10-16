"""
Functions - defining, calling
Function  arguments : positional, keyword, default, variable -length
Return statement

Functions in Python

A function is a block of reusable code that performs a specific task.
We use def keyword to define a function.
"""

# 1. Defining and Calling a Function
# Defining a function
def greet():
    print("Hello, welcome to Python functions!")

# Calling the function
greet()

#2. Function Arguments
#(a) Positional Arguments
#Values are passed in order.

def add(a, b):
    print("Sum:", a + b)

add(10, 20)   # a=10, b=20

#(b) Keyword Arguments
#Specify arguments by name.
#Order doesn’t matter.

def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=25, name="Alice")

#(c) Default Arguments
#If no value is passed, the default is used.
def greet(name="Guest"):
    print("Hello,", name)

greet()           # uses default
greet("Sakshi") # overrides default

#(d) Variable-Length Arguments
#i. *args → (non-keyword variable-length, stored as a tuple)
def sum_all(*args):
    total = sum(args)
    print("Sum:", total)

sum_all(1, 2, 3, 4, 5)

# skip this
#ii. **kwargs → (keyword variable-length, stored as a dictionary)
def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_details(name="Alice", age=25, city="New York")

#3. Return Statement
#Used to return a value from a function.

def square(num):
    return num * num

result = square(6)
print("Square:", result)

# 5 Practice Problems with Code
#Q1. Write a function to calculate factorial of a number
#Q2. Write a function that takes variable-length arguments and returns the maximum
#Q3. Function with default arguments to calculate power
# Q4. Write a function that accepts a dictionary (kwargs) and prints key-value pairs
# Q5  Function to check if a number is prime


#Q1. Write a function to calculate factorial of a number

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print("Factorial of 5:", factorial(5))

#Q2. Write a function that takes variable-length arguments and returns the maximum
def find_max(*args):
    return max(args)

print("Max value:", find_max(10, 20, 5, 40, 15))

#Q3. Function with default arguments to calculate power
def power(base, exp=2):
    return base ** exp

print("Square:", power(5))
print("Cube:", power(5, 3))

# Q4. Write a function that accepts a dictionary (kwargs) and prints key-value pairs
def print_student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_student_details(name="Ravi", age=21, grade="A")

# Q5  Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Is 7 prime?", is_prime(7))
print("Is 12 prime?", is_prime(12))
