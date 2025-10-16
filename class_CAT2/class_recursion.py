"""
Recursion
1. What is Recursion?

Recursion is when a function calls itself directly or indirectly.

It is used to solve problems by breaking them into smaller, similar subproblems.

Every recursive function has two parts:

Base Case → The condition that stops recursion (prevents infinite loop).

Recursive Case → The part where the function calls itself.
"""

# Example: Factorial using Recursion
def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:
        return n * factorial(n - 1)   # Recursive case

print(factorial(5))   # 120

# Example: Fibonacci Sequence using Recursion
def fibonacci(n):
    if n <= 1:   # Base case
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(i) for i in range(6)])  # [0, 1, 1, 2, 3, 5]

# 5 Practice Problems with Code
# Q1. Sum of first N natural numbers using recursion
# Q2. Reverse a string using recursion
# Q3. Find Greatest Common Divisor (GCD) using recursion
# Q4. Check if a number is a palindrome using recursion
# Q5. Power function using recursion (x^n)


# Q1. Sum of first N natural numbers using recursion
def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n-1)

print(sum_n(10))   # 55

# Q2. Reverse a string using recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))   # 'olleh'

# Q3. Find Greatest Common Divisor (GCD) using recursion
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(48, 18))   # 6

# Q4. Check if a number is a palindrome using recursion
def is_palindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])

print(is_palindrome("madam"))   # True
print(is_palindrome("hello"))   # False

# Q5. Power function using recursion (x^n)
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

print(power(2, 5))   # 32

