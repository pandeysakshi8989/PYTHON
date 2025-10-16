# Recursion - Calculating Factorials for the Space Expedition

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

n = int(input())
print(factorial(n))

# Recursion - Calculating the Total Revenue of Orders

def total_revenue(n):
    if n == 1:
        return 1
    return n + total_revenue(n - 1)

n = int(input())
print(total_revenue(n))

# Recursion - The Fibonacci Sequence for Future Engineers

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())
print(fibonacci(n))

# Recursion - Finding the Greatest Common Divisor in Ancient Math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a, b = map(int, input().split())

print(gcd(a, b))

# Recursion - Finding the Mighty Element in the Forest

def find_max(arr, n):
    if n == 1:
        return arr[0]
    
    return max(arr[n-1], find_max(arr, n-1))

n = int(input())
arr = list(map(int, input().split()))
print(find_max(arr, n))

# Recursion - Counting Active Bits in a Device Monitoring System

def countSetBits(number):
    if number == 0:
        return 0
    return (number % 2) + countSetBits(number // 2)

num = int(input())
print(countSetBits(num))

# Recursion - Recursive String Length Calculator
def stringLength(s):
    if s == "":
        return 0
    return 1 + stringLength(s[1:])

s = input()
print(stringLength(s))

# Recursion - Recursive Sum of Array Elements

def arraySum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + arraySum(arr[1:])

n = int(input())
arr = list(map(int, input().split()))
print(arraySum(arr))

# Recursion - Recursive Calculation of Power of 2

def powerOfTwo(n):
    if n == 0:
        return 1
    return 2 * powerOfTwo(n - 1)

n = int(input())
print(powerOfTwo(n))

# Recursion - Validating Account Numbers

def countDigits(n):
    if n < 10:
        return 1
    return 1 + countDigits(n // 10)

n = int(input())
print(countDigits(n))

