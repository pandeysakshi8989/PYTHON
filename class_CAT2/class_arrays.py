# """

# Arrays 1D
# Arrays 2D
# Arrays functions

# 1. 1D Arrays in Python

# A 1D array is a linear structure where elements are stored in a single row.
# In Python, arrays can be implemented using the array module or NumPy (most common).

# """
# #Using array module
# import array as arr

# # Creating a 1D array of integers
# numbers = arr.array('i', [10, 20, 30, 40, 50])

# print("Array elements:")
# for num in numbers:
#     print(num, end=" ")
# print()
# print(numbers[0])

# # # Accessing elements
# print("First element:", numbers[0])   # 10
# print("Last element:", numbers[-1])  # 50

# # 2D Arrays in Python
# #Python doesn’t have built-in 2D arrays, but we can use nested lists or NumPy.
# # using list
# # 2D array (matrix)
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print("Element at row 2, col 3:", matrix[1][2])  # 6
# #print 8
# print()
# print("Elements at row 3 and column 2:",matrix[2][1])

# SKIP THIS
# #using numpy
# import numpy as np

# # Creating a 2D NumPy array
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print("Matrix:\n", matrix)
# print("Element [2,3]:", matrix[1, 2])  # 6

# #Array Functions
# #with array module
import array as arr

nums = arr.array('i', [10, 20, 30, 40]) # strat with index 0
print(nums) # [10,20,30,40]
nums.append(50) # add elemennt in the last
print(nums)       #  [ 10,20,30,40,50]
nums.insert(2, 25)    #insert element at (index, element)
print(nums) # [10,20,25,30,40,50]
nums.remove(30) # remove at particular element
print(nums) # [10,20,40,50]
nums.pop()   # remove last element         
print(nums) # [10,20,30,40]

# SKIP THS
# #with numpy
# import numpy as np

# a = np.array([10, 20, 30, 40])

# print("Sum:", np.sum(a))           # 100
# print("Mean:", np.mean(a))         # 25.0
# print("Max:", np.max(a))           # 40
# print("Min:", np.min(a))           # 10
# print("Sorted:", np.sort(a))       # [10 20 30 40]

# #2d array functions
# matrix = np.array([[1, 2, 3], [4, 5, 6]])

# print("Shape:", matrix.shape)       # (2,3)
# print("Transpose:\n", matrix.T)     # Rows ↔ Columns
# print("Sum of rows:", np.sum(matrix, axis=1))  # [6 15]
# print("Sum of cols:", np.sum(matrix, axis=0))  # [5 7 9]

# # practice problems
# #Q1. Create a 1D array and find the sum of all elements
# # Q2. Find the maximum and minimum elements in an array
# # Q3. Reverse a 1D array
# # Q4. Create a 2D array (matrix) and find the transpose
# # Q5 Find row-wise and column-wise sum of a 2D array


# # practice problems
# #Q1. Create a 1D array and find the sum of all elements

# import array as arr
# import numpy as np

# # Using array module
# nums = arr.array('i', [5, 10, 15, 20, 25])
# print("Sum (array module):", sum(nums))

# # Using NumPy
# nums_np = np.array([5, 10, 15, 20, 25])
# print("Sum (NumPy):", np.sum(nums_np))

# # Q2. Find the maximum and minimum elements in an array
# import array as arr
# import numpy as np

# # Using array module
# nums = arr.array('i', [12, 45, 7, 34, 89, 23])
# print("Max:", max(nums))
# print("Min:", min(nums))

# # Using NumPy
# nums_np = np.array([12, 45, 7, 34, 89, 23])
# print("Max (NumPy):", np.max(nums_np))
# print("Min (NumPy):", np.min(nums_np))

# # Q3. Reverse a 1D array
# import array as arr
# import numpy as np

# # Using array module
# nums = arr.array('i', [1, 2, 3, 4, 5])
# nums.reverse()
# print("Reversed (array module):", nums)

# # Using NumPy
# nums_np = np.array([1, 2, 3, 4, 5])
# print("Reversed (NumPy):", nums_np[::-1])

# # Q4. Create a 2D array (matrix) and find the transpose
# import numpy as np

# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print("Original Matrix:\n", matrix)
# print("Transpose:\n", matrix.T)

# # Q5 Find row-wise and column-wise sum of a 2D array
# import numpy as np

# matrix = np.array([[2, 4, 6], [1, 3, 5], [7, 8, 9]])

# print("Matrix:\n", matrix)

# # Row-wise sum
# print("Row-wise sum:", np.sum(matrix, axis=1))

# # Column-wise sum
# print("Column-wise sum:", np.sum(matrix, axis=0))

