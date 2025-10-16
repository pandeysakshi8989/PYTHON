# Problems on while Loop

# Print 1 to 10
# Write a program using while loop to print numbers from 1 to 10.
i=1
while(i<=10):
    print(i)

# Sum of first N numbers
# Take an integer N from user and find the sum of first N natural numbers using while.
N = int(input())
i =1
sum =0
while(i<= N):
    sum+=1
print(sum)

# Reverse a Number
# Take an integer as input and print its reverse using while.
num = int(input("Enter a number: "))   # Input number
rev = 0                                # Variable to store reverse

while num > 0:                         # Loop until number becomes 0
    digit = num % 10                   # Get last digit
    rev = rev * 10 + digit             # Build reverse number
    num = num // 10                    # Remove last digit from num

print("Reversed Number:", rev)


# Count Digits
# Take a number as input and count how many digits it has using while.
num = int(input("Enter a number: "))   # Input number
count = 0                              # Initialize counter

if num == 0:                           # Special case for 0
    count = 1
else:
    while num > 0:                     # Loop until number becomes 0
        count += 1                     # Increment count
        num = num // 10                # Remove last digit

print("Total digits:", count)

# Factorial
# Find factorial of a given number using while loop.
num = int(input("Enter a number: "))   # Input number
fact = 1                               # Initialize factorial
i = 1                                  # Counter

while i <= num:                        # Loop from 1 to num
    fact = fact * i
    i += 1

print("Factorial of", num, "is:", fact)

# Table of a Number
# Take a number as input and print its multiplication table (1–10) using while.
num = int(input("Enter a number: "))   # Input number
i = 1                                  # Counter starts from 1

while i <= 10:                         # Loop until 10
    print(num, "x", i, "=", num * i)   # Print table line
    i += 1


# Even Numbers in Range
# Print all even numbers between 1 and 50 using while.
i = 2   # Start from first even number
while i <= 50:
    print(i, end=" ")
    i += 2   # Increment by 2 to get next even number


# Palindrome Number
# Check if a given number is palindrome (same forward & backward) using while.
num = int(input("Enter a number: "))   # Input number
temp = num                             # Store original number
rev = 0                                # Variable for reverse

while num > 0:                         # Loop until number becomes 0
    digit = num % 10                   # Get last digit
    rev = rev * 10 + digit             # Build reversed number
    num = num // 10                    # Remove last digit
if temp == rev:                        # Check palindrome
    print(temp, "is a Palindrome number")
else:
    print(temp, "is NOT a Palindrome number")

# Sum of Digits
# Find sum of digits of a given number using while.
num = int(input("Enter a number: "))   # Input number
total = 0                              # Initialize sum
while num > 0:                         # Loop until number becomes 0
    digit = num % 10                   # Extract last digit
    total += digit                     # Add digit to sum
    num = num // 10                    # Remove last digit
print("Sum of digits =", total)

# Guessing Game
# Generate a secret number between 1 and 10. Keep asking the user to guess until correct (using while).
import random

secret = random.randint(1, 10)      # Generate secret number
guess = 0                           # Initialize guess

while guess != secret:              # Loop until guess is correct
    guess = int(input("Guess the number (1-10): "))
    
    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print("Correct! The secret number was", secret)


# Problems on for Loop

# Print 1 to N
# Take N from user and print numbers from 1 to N using for.
N = int(input("Enter a number: "))
for i in range(1, N+1):
    print(i, end=" ")

# Squares of Numbers
# Print squares of numbers from 1 to 20 using for.
for i in range(1, 21):
    print(i, "squared is", i**2)

# Sum of Even Numbers
# Find sum of even numbers between 1 and 100 using for.
total = 0
for i in range(2, 101, 2):   # step of 2 → only even
    total += i
print("Sum of even numbers from 1 to 100 =", total)

# Multiplication Table
# Take a number and print its multiplication table using for.
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Factorial
# Find factorial of a number using for loop.
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num+1):
    fact *= i
print("Factorial of", num, "is", fact)

# Fibonacci Series
# Print first N terms of Fibonacci sequence using for.
N = int(input("Enter number of terms: "))
a, b = 0, 1
for i in range(N):
    print(a, end=" ")
    a, b = b, a+b

# Prime Number Check
# Check if a number is prime using for.
num = int(input("Enter a number: "))
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):  # check till sqrt(num)
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "is a Prime number")
else:
    print(num, "is NOT a Prime number")

# Pattern Printing (Stars)
# Print the following using for:
# *
# **
# ***
# ****
# *****
for i in range(1, 6):
    print("*" * i)

# List Sum
# Given a list of numbers, find their sum using for.
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print("Sum of list elements =", total)

# Count Vowels in String
# Take a string input and count vowels (a, e, i, o, u) using for.
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels in string =", count)

# Find the first multiple of 7 greater than 50
num = 51
while True:
    if num % 7 == 0:
        print("First multiple of 7 greater than 50 is:", num)
        break
    num += 1

# Print numbers from 1 to 20 except multiples of 5
for i in range(1, 21):
    if i % 5 == 0:
        continue
    print(i, end=" ")

# Check if a number is prime using for...else
num = int(input("Enter a number: "))
for i in range(2, num):
    if num % i == 0:
        print(num, "is NOT Prime")
        break
else:
    print(num, "is Prime")

# Search for a number in a list
numbers = [10, 20, 30, 40, 50]
key = int(input("Enter number to search: "))
for n in numbers:
    if n == key:
        print("Found", key)
        break
else:
    print("Not Found")

# Guess number game with break
secret = 7
while True:
    guess = int(input("Guess the number (1-10): "))
    if guess == secret:
        print("Correct!")
        break
    else:
        print("Try again...")

# Print even numbers 1 to 20 using continue in while
i = 0
while i <= 20:
    i += 1
    if i % 2 != 0:
        continue
    print(i, end=" ")

# Allow 3 attempts for password, else block runs if no break
password = "python123"
for attempt in range(3):
    guess = input("Enter password: ")
    if guess == password:
        print("Access Granted ")
        break
else:
    print("Access Denied  (3 wrong attempts)")

# Find first negative number in list
nums = [4, 7, 9, -3, -6, 10]
for n in nums:
    if n < 0:
        print("First negative number is:", n)
        break

# Skip numbers not divisible by 3 until 30
i = 0
while i <= 30:
    i += 1
    if i % 3 != 0:
        continue
    print(i, end=" ")

# Search for a character in string
text = "hello world"
ch = input("Enter character to search: ")

for c in text:
    if c == ch:
        print("Character found:", c)
        break
else:
    print("Character not found")
