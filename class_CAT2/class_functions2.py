"""

Scope and Lifetime of varibles
Built-in functions
User defined functions

1. Scope and Lifetime of Variables
Scope

The scope of a variable determines where it can be accessed in the program.
Python has LEGB Rule (Local → Enclosing → Global → Built-in).

Local: Inside a function.

Global: Declared outside all functions, accessible everywhere.

Enclosing: In nested functions.

Built-in: Predefined names in Python (len, sum, etc.).
"""

x = 100  # Global variable

def test_scope():
    y = 50  # Local variable
    print("Inside function: x =", x, ", y =", y)

test_scope()
print("Outside function: x =", x)  # y not accessible here

#Lifetime
#A global variable exists until the program ends.
#A local variable exists only while the function is executing.

def my_func():
    temp = 10  # Local variable (lifetime = during function call)
    print("Inside function:", temp)

my_func()
# print(temp)  #  Error: temp not defined

# 2. Built-in Functions
#Python provides many built-in functions that can be used directly.

print("Length:", len([1, 2, 3, 4]))  # 4
print("Maximum:", max(10, 20, 30))   # 30
print("Minimum:", min(10, 20, 30))   # 10
print("Sum:", sum([5, 10, 15]))      # 30
print("Absolute:", abs(-25))         # 25

# 3. User-Defined Functions
#A user-defined function is created by the programmer using def.

def greet(name):
    return f"Hello, {name}!"

print(greet("Sakshi"))

#5 Practice Problems with Code
# Q1. Demonstrate global vs local variable
# Q2. Write a function to calculate the factorial of a number using a user-defined function
# Q3. Use built-in functions to find sum, max, min of a list
# Q4. Create a user-defined function that returns both square and cube of a number
# Q5. Demonstrate local variable lifetime with function calls


# Q1. Demonstrate global vs local variable

x = 10  # Global

def modify():
    global x   # use global variable
    x = x + 5
    print("Inside function:", x)

modify()
print("Outside function:", x)

# Q2. Write a function to calculate the factorial of a number using a user-defined function

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print("Factorial of 6:", factorial(6))

# Q3. Use built-in functions to find sum, max, min of a list

numbers = [12, 45, 7, 23, 89]

print("Sum:", sum(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))

# Q4. Create a user-defined function that returns both square and cube of a number

def square_cube(n):
    return n**2, n**3

sq, cu = square_cube(5)
print("Square:", sq, "Cube:", cu)

# Q5. Demonstrate local variable lifetime with function calls
def counter():
    count = 0   # Local variable, resets each call
    count += 1
    print("Count:", count)

counter()
counter()
counter()

