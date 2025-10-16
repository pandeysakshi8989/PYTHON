# Problem on Operators

#Take two numbers as input and print their sum, difference, product, and quotient.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)
print("Difference =", a - b)
print("Product =", a * b)
print("Quotient =", a / b)

# Find the remainder when one number is divided by another.
a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))

print("Remainder =", a % b)

# Take a number and print its square and cube.
num = int(input("Enter a number: "))

print("Square =", num ** 2)
print("Cube =", num ** 3)

# Convert total minutes ipnto hours and minutes using // and %.
minutes = int(input("Enter total minutes: "))

hours = minutes // 60
rem_minutes = minutes % 60

print("Hours:", hours, "Minutes:", rem_minutes)

# Take length and breadth of a rectangle, calculate area and perimeter.
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area =", area)
print("Perimeter =", perimeter)

# Write a program to calculate the compound interest.
P = float(input("Enter Principal: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time (in years): "))

A = P * (1 + R/100) ** T
CI = A - P

print("Compound Interest =", CI)

# Write a program to calculate simple interest.
P = float(input("Enter Principal: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time (in years): "))

SI = (P * R * T) / 100
print("Simple Interest =", SI)

# Problem of creating your own calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Choose operation: +, -, *, /")
op = input("Enter operator: ")

if op == "+":
    print("Result =", a + b)
elif op == "-":
    print("Result =", a - b)
elif op == "*":
    print("Result =", a * b)
elif op == "/":
    print("Result =", a / b)
else:
    print("Invalid Operator!")

# Problem of swapping two variables
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Before Swap: x =", x, "y =", y)

# swapping
x, y = y, x

print("After Swap: x =", x, "y =", y)

# Problem of conversion of Fareheit to Celsius
F = float(input("Enter temperature in Fahrenheit: "))

C = (F - 32) * 5 / 9

print("Temperature in Celsius =", C)


#Take a number and increment it by 10 using +=.
num = int(input("Enter a number: "))
num += 10
print("After increment by 10:", num)

#Take a number and multiply it by 5 using *= and print the result.
num = int(input("Enter a number: "))
num *= 5
print("After multiplying by 5:", num)

#Take a variable x = 50, reduce it by 15 using -= and print.
x = 50
x -= 15
print("After reducing by 15:", x)

#Take a variable, divide it by 3 using /= and print.
num = float(input("Enter a number: "))
num /= 3
print("After division by 3:", num)

#Take a variable, perform floor division by 4 using //= and print.
num = int(input("Enter a number: "))
num //= 4
print("After floor division by 4:", num)

#Take a number, find its square using **=.
num = int(input("Enter a number: "))
num **= 2
print("Square of number:", num)

# Compare two numbers and print which is greater.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("Both are equal")

# Check if two strings are equal.
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s1 == s2:
    print("Strings are equal")
else:
    print("Strings are not equal")

# Take a number and check if it is not equal to 100.
num = int(input("Enter a number: "))

if num != 100:
    print("Number is not equal to 100")
else:
    print("Number is 100")

# Take a number and check if it's greater than 50.
num = int(input("Enter a number: "))

if num > 50:
    print("Number is greater than 50")
else:
    print("Number is not greater than 50")

# Take two numbers and check if the first is less than or equal to the second.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a <= b:
    print("First number is less than or equal to second")
else:
    print("First number is greater than second")

# Check if three numbers are in ascending order. 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b < c:
    print("Numbers are in ascending order")
else:
    print("Numbers are not in ascending order")

# Take two boolean values from the user and print the result of AND, OR, and
# NOT operations.
a = bool(int(input("Enter first boolean (1 for True, 0 for False): ")))
b = bool(int(input("Enter second boolean (1 for True, 0 for False): ")))

print("a AND b =", a and b)
print("a OR b =", a or b)
print("NOT a =", not a)
print("NOT b =", not b)

# Check if a number is positive and even using and.
num = int(input("Enter a number: "))

if num > 0 and num % 2 == 0:
    print("Number is positive and even")
else:
    print("Condition not satisfied")

# Check if a number is positive or a multiple of 5 using or.
num = int(input("Enter a number: "))

if num > 0 or num % 5 == 0:
    print("Number is positive or multiple of 5")
else:
    print("Condition not satisfied")

# Check if a number is not negative using not.
num = int(input("Enter a number: "))

if not (num < 0):
    print("Number is not negative")
else:
    print("Number is negative")

# Take a number and check if it lies between 10 and 50 (inclusive) using logical operators.
num = int(input("Enter a number: "))

if num >= 10 and num <= 50:
    print("Number lies between 10 and 50")
else:
    print("Number is outside the range")

# Check if a person is eligible to vote (age >= 18) and a senior citizen (age >70).
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

if age > 70:
    print("Person is a Senior Citizen")
else:
    print("Not a Senior Citizen")
