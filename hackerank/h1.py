# Basic I/O
# Input & Output - Automated System Greeting for New Users
print("Hello, World!")

#Input & Output - Automated Coffee Machine Startup with Repeated Humorous Message
print("I need coffee too!!")
print("I need coffee too!!")
print("I need coffee too!!")

#Input & Output - Customer Service System Welcome Screen
name = input()
print("Welcome",name)

#Input & Output - Student Information Management System
Name=str(input())
Age=int(input())
CGPA=float(input())
Grade=input()

import math
CGPA_new = math.trunc(CGPA *100)/100
print(f"Name: {Name}")
print(f"Age: {Age}")
print(f"CGPA: {CGPA_new:.2f}")
print(f"Grade: {Grade}")

#Input & Output - User Registration System
age = int(input())
name = input()
print("User Details:")
print("Name:",name)
print("Age:",age)

#Input & Output - Gym Membership Registration System
name = input()
membership = input()
print("Member Name:", name)
print("Selected Membership:",membership)

#Input & Output - Character Analysis Tool
x = input()[0] # input takes string by default # 'a',' A'
# input()[0] means take only first character of string
ascii_value = ord(x) # ord function for converting charcter to ascii value
print(ascii_value)

#Input & Output - ASCII Decoder Tool
ch = int(input())
print(chr(ch))

#Input & Output - Financial Application for Rounding Values
a = float(input())
import math
print(math.trunc(a))
print(math.ceil(a))
print(math.floor(a))

#Input & Output - Mathematical Operations Calculator
first = float(input())
second = float(input())
print("Square Root of first number:",pow(first,0.5))
print("First number raised to the power of second number:",pow(first,second))
print("Absolute value of first number:",abs(first))
print("Absolute value of second number:",abs(second))