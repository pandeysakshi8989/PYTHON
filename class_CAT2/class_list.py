# """
# 1. What is a List in Python?

# A list is a collection in Python that is:

# Ordered (items have a fixed order)

# Mutable (can be changed after creation)

# Allows duplicates

# Can hold different data types (e.g., int, str, float, even other lists).

# List -creation, indexing, slicing, nested lists
# List comprehension
# List functions

# """
# # 1. List creation
# # # Empty list
# empty_list = []
# print(empty_list)
# # List with elements
# fruits = ["apple", "banana", "cherry"]
# print(fruits)
# # Mixed data types
# mixed = [1, "hello", 3.5, True]
# print(mixed)
# # From range
# numbers = list(range(5))
# print(numbers)  # [0, 1, 2, 3, 4]               

# # 2 Indexing in Lists
# fruits = ["apple", "banana", "cherry", "mango"]
# print(fruits[0])   # apple (first element)
# print(fruits[-1])  # mango (last element)
# print(fruits[2])   # cherry
    
# #3 Slicing in Lists
# nums = [10, 20, 30, 40, 50]

# print(nums[1:4])   # [20, 30, 40]
# print(nums[:3])    # [10, 20, 30]
# print(nums[2:])    # [30, 40, 50]
# print(nums[::-1])  # [50, 40, 30, 20, 10] (reversed)

# #4 Nested Lists
# matrix = [[1, 2], [3, 4], [5, 6]]

# print(matrix[0])     # [1, 2]
# print(matrix[1][1])  # 4
# print(matrix[2][0])  # 5

# #5 List Comprehension
# # Squares of numbers
# squares = [x**2 for x in range(1, 6)]
# print(squares)  # [1, 4, 9, 16, 25]

# # Even numbers
# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)  # [0, 2, 4, 6, 8]

# # Words in uppercase
# words = ["hello", "world"]
# upper = [w.upper() for w in words]
# print(upper)  # ['HELLO', 'WORLD']

# #Common List Functions & Methods
# nums = [1, 2, 3, 4, 2]

# print(len(nums))        # 5 (length of list)
# print(max(nums))        # 4
# print(min(nums))        # 1
# print(sum(nums))        # 12

# nums.append(5)          # add element
# print(nums)             # [1, 2, 3, 4, 2, 5]

# nums.insert(2, 99)      # insert at index 2
# print(nums)             # [1, 2, 99, 3, 4, 2, 5]

# nums.remove(2)          # remove first occurrence of 2
# print(nums)             # [1, 99, 3, 4, 2, 5]

# print(nums.count(2))    # 1 (count of 2)

# nums.sort()
# print(nums)             # [1, 2, 3, 4, 5, 99]

# nums.reverse()
# print(nums)             # [99, 5, 4, 3, 2, 1]

# copy_list = nums.copy()
# nums.clear()
# print(copy_list)        # [99, 5, 4, 3, 2, 1]
# print(nums)             # []

# # Practice Problems on Lists
# #Q1. Create a list of the first 10 natural numbers and print only the odd numbers using list comprehension.
# #Q2. Given a list of numbers, find the largest and second largest number without using max() twice.
# #Q3. Create a nested list of 3x3 (matrix form) and access the element in the second 
# #Q4. Write a program to remove duplicates from a list while keeping the order.
# #Q5. Given a list of strings, generate a new list containing the length of each string.

# # Practice Problems on Lists
# #Q1. Create a list of the first 10 natural numbers and print only the odd numbers using list comprehension.
# # First 10 natural numbers
# numbers = list(range(1, 11))

# # List comprehension for odd numbers
# odd_numbers = [x for x in numbers if x % 2 != 0]

# print("Odd numbers:", odd_numbers)

# #Q2. Given a list of numbers, find the largest and second largest number without using max() twice.
# nums = [10, 25, 8, 56, 75, 56, 32]

# largest = second = float('-inf')  

# for n in nums:
#     if n > largest:
#         second = largest
#         largest = n
#     elif n > second and n != largest:
#         second = n

# print("Largest:", largest)
# print("Second Largest:", second)

# #Q3. Create a nested list of 3x3 (matrix form) and access the element in the second row, third column.
# # 3x3 matrix
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# element = matrix[1][2]  # row index 1 (second row), col index 2 (third column)

# print("Matrix:", matrix)
# print("Element at 2nd row, 3rd column:", element)

# #Q4. Write a program to remove duplicates from a list while keeping the order.
# nums = [10, 20, 10, 30, 20, 40, 50, 30]

# unique = []
# for n in nums:
#     if n not in unique:
#         unique.append(n)

# print("Original list:", nums)
# print("After removing duplicates:", unique)

# #Q5. Given a list of strings, generate a new list containing the length of each string.
# words = ["python", "java", "c++", "machinelearning"]

# lengths = [len(word) for word in words]

# print("Words:", words)
# print("Lengths:", lengths)
