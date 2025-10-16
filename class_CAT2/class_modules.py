"""

# 🔹 **1. What are Modules in Python?**
# * A **module** is a file that contains Python code (functions, variables, classes).
# * It helps in **organizing code** into manageable sections and allows **code reuse**.
# * You can import and use modules in other Python files.


# 🔹 **2. Types of Modules**
#1. **Built-in modules** → Already included in Python (e.g., `math`, `random`, `os`).
#2. **User-defined modules** → Created by programmers.


# 🔹 **3. Using Built-in Modules**

import math

print(math.sqrt(16))     # 4.0
print(math.factorial(5)) # 120
print(math.pi)           # 3.141592653589793


# 🔹 **4. Using `from` keyword**

from math import sqrt, pi

print(sqrt(25))   # 5.0
print(pi)         # 3.141592653589793


# 🔹 **5. User-Defined Module**

# Create a file called **my\_module.py**
# my_module.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

# Use this module in another file:
import my_module

print(my_module.greet("Sonalika"))   # Hello, Sonalika!
print(my_module.add(5, 3))           # 8

# 🔹 **6. 5 Practice Problems with Code**

## **Q1. Use the `random` module to generate 5 random numbers between 1 and 50**

import random

nums = [random.randint(1, 50) for _ in range(5)]
print(nums)

## **Q2. Use the `datetime` module to print today’s date and current time**

import datetime

now = datetime.datetime.now()
print("Current date and time:", now)
print("Today's date:", now.date())

## **Q3. Create a user-defined module with a function that calculates area of circle**
# **circle\_module.py**
def area_circle(radius):
    import math
    return math.pi * radius * radius

# **main.py**
import circle_module
print(circle_module.area_circle(7))   # 153.93804002589985

## **Q4. Use the `os` module to print current working directory**

import os

print("Current Working Directory:", os.getcwd())

## **Q5. Use the `statistics` module to calculate mean, median, mode**
import statistics

data = [2, 4, 6, 8, 4, 2, 10]
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))

"""
