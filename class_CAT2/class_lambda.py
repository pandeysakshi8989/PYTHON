"""
Lambda Expressions

1. What are Lambda Expressions?

A lambda expression is a small, anonymous function in Python.

Defined using the keyword lambda.

Syntax:

lambda arguments: expression

Used when you need a quick one-line function without formally defining it with def.
"""

# Normal function
def add(x, y):
    return x + y

print(add(5, 3))   # 8

# Lambda equivalent
add_lambda = lambda x, y: x + y
print(add_lambda(5, 3))   # 8

#Where are Lambdas Useful?
#With built-in functions like map(), filter(), reduce(), sorted()

# Double each number using map
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)   # [2, 4, 6, 8, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)   # [2, 4]

# Sort by length of words
words = ["python", "is", "awesome"]
sorted_words = sorted(words, key=lambda w: len(w))
print(sorted_words)   # ['is', 'python', 'awesome']

# 4. Practice Problems
#Q1. Find square of a number using lambda
# Q2. Sort a list of tuples based on the second element
# Q3. Use lambda with filter() to extract numbers greater than 10
# Q4. Multiply each element in a list by 3 using map()
#Q5. Find the maximum element in a list of tuples based on second value


#Q1. Find square of a number using lambda

square = lambda x: x ** 2
print(square(6))   # 36

# Q2. Sort a list of tuples based on the second element
pairs = [(1, 5), (3, 2), (2, 8)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)   # [(3, 2), (1, 5), (2, 8)]

# Q3. Use lambda with filter() to extract numbers greater than 10
nums = [5, 12, 7, 18, 3, 25]
greater_than_10 = list(filter(lambda x: x > 10, nums))
print(greater_than_10)   # [12, 18, 25]

# Q4. Multiply each element in a list by 3 using map()
nums = [2, 4, 6, 8]
triple = list(map(lambda x: x * 3, nums))
print(triple)   # [6, 12, 18, 24]

#Q5. Find the maximum element in a list of tuples based on second value
pairs = [(1, 10), (2, 25), (3, 15)]
max_pair = max(pairs, key=lambda x: x[1])
print(max_pair)   # (2, 25)
