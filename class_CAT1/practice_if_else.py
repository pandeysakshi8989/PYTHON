# Problem Statements of Decision making

# Problem: Are you tall? check height greater than 185cm 
height = input('What is your height in centimeters? ')
if int(height) > 185:
    print('You are very tall')

# Problem: Python program to check if the number is divisible by 5 or not
d = int(input("Enter a number: "))
if (d%5 == 0):
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")

# Problem: Write program to check whether a person is elligible for vote or not 
age = int(input("Enter your age: "))
if(age >= 18):
    print("You are elligible for voting")
else:
    print("You are not elligible for voting")

# Problem: Python program to check if the number is odd or even
number = int(input("Enter a number: "))
if number%2 == 0:
    print("Given number is Even")
else:
    print("Given number is Odd")

# Problem: Python program to check if the number is divisible by both 5 and 7 or not
number = int(input("Enter a number: "))
if (number%5 == 0) and (number%7 == 0):
    print("Number is divisible by both 5 and 7")
else:
    print("Number is not divisible by both 5 and 7")

# Problem: Is Sydney the capital of Australia?
answer = input('Is Sydney the capital of Australia? ')
if answer == 'y':
    print('Wrong! Canberra is the capital!')
elif answer == 'n':
    print('Correct!')
else:
    print('I do not understand your answer!')

# Problem: Write a program that asks the user for a year and replies with either leap year or not a leap year.
year = int(input('Provide a year: '))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print('leap year')
        else:
            print('not a leap year')
    else:
        print('leap year')
else:
     print('not a leap year')

# Problem: Write a program to check if last digit of number entered is divisible by 3 or not
num = int(input("Enter a number: "))
last_digit = num % 10

if last_digit % 3 == 0:
    print("Last digit", last_digit, "is divisible by 3")
else:
    print("Last digit", last_digit, "is NOT divisible by 3")

# Problem: Write a program to give grade if >90 - A, <90 and >80 -B, <80 and >60 - C, <60 - D

marks = int(input("Enter marks: "))

if marks > 90:
    print("Grade: A")
elif marks > 80:
    print("Grade: B")
elif marks > 60:
    print("Grade: C")
else:
    print("Grade: D")

# Problem: Accept number 1 to 7 and display days of week
day = int(input("Enter number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid Input! Enter 1-7 only.")

# Problem: Accept any city and display monument of city
city = input("Enter city name: ").lower()

if city == "agra":
    print("Monument: Taj Mahal")
elif city == "delhi":
    print("Monument: Red Fort")
elif city == "jaipur":
    print("Monument: Hawa Mahal")
elif city == "mumbai":
    print("Monument: Gateway of India")
else:
    print("Monument information not available for", city.title())

# Problem: Find largest number out of three numbers 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

# PS1: Write a program to calculate electricity bill
# First 100 units - no charge
# Next 100 units - Rs 5 per  unit charge
# After 200 units - Rs 10 per unit charge 
# Minium Rs. 100 have to pay by everyone if if unit is less than 100

units = int(input("Enter units consumed: "))

if units <= 100:
    bill = 100   # minimum charge
elif units <= 200:
    bill = 100 + (units - 100) * 5
else:
    bill = 100 + (100 * 5) + (units - 200) * 10

print("Electricity Bill = Rs.", bill)

# Check if Number is Positive, Negative, or Zero
# Nested if-else
num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Number is Zero")
    else:
        print("Number is Positive")
else:
    print("Number is Negative")

# Check if Number is Even or Odd, and Divisible by 5
num = int(input("Enter a number: "))

if num % 2 == 0:
    if num % 5 == 0:
        print("Even and divisible by 5")
    else:
        print("Even but not divisible by 5")
else:
    print("Odd number")

# Check if Character is Alphabet, Digit, or Special Character
ch = input("Enter a character: ")

if ch.isalpha():
    if ch.isupper():
        print("Uppercase Alphabet")
    else:
        print("Lowercase Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")

# Find Largest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b:
    if a >= c:
        print("Largest is:", a)
    else:
        print("Largest is:", c)
else:
    if b >= c:
        print("Largest is:", b)
    else:
        print("Largest is:", c)

# Student Result (Pass/Fail with Distinction)
marks = int(input("Enter marks: "))

if marks >= 40:
    if marks >= 75:
        print("Pass with Distinction")
    else:
        print("Pass")
else:
    print("Fail")

# Check Even or Odd
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

# Find Greater of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a if a > b else b, "is greater")

# Check Vowel or Consonant
ch = input("Enter a character: ").lower()
print("Vowel" if ch in "aeiou" else "Consonant")

# Absolute Value of Number
num = int(input("Enter a number: "))
print(num if num >= 0 else -num)

# Eligible to Vote (≥18) or Not
age = int(input("Enter your age: "))
print("Eligible to Vote" if age >= 18 else "Not Eligible")
