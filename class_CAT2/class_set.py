# """
# Set - uniqueness, set operations
# Set in Python

# A set is an unordered collection of unique elements.

# ✅ Key Features

# Uniqueness → Duplicate values are automatically removed.

# Unordered → Elements don’t have a fixed position (no indexing).
# """

# # Creating a set
# my_set = {1, 2, 3, 3, 4, 5}
# print(my_set)   # {1, 2, 3, 4, 5} → duplicates removed

# # Set operations
# # 1. Union
# A = {1, 2, 3}
# B = {3, 4, 5}

# print(A | B)           # {1, 2, 3, 4, 5}
# print(A.union(B))      # {1, 2, 3, 4, 5}

# # 2. Intersection
# A = {1, 2, 3}
# B = {2, 3, 4}

# print(A & B)                # {2, 3}
# print(A.intersection(B))    # {2, 3}

# #3. Difference
# A = {1, 2, 3, 4}
# B = {3, 4, 5}

# print(A - B)                # {1, 2}
# print(B - A)                # {5}

# #4. Symmetric Difference
# A = {1, 2, 3}
# B = {3, 4, 5}

# print(A ^ B)                         # {1, 2, 4, 5}
# print(A.symmetric_difference(B))     # {1, 2, 4, 5}

# #5. Subset and Superset
# A = {1, 2}
# B = {1, 2, 3, 4}

# print(A.issubset(B))     # True
# print(B.issuperset(A))   # True

# #Practice problems on Set
# # 1.Remove duplicates from a list using a set
# #2. Find common elements between two lists using sets
# #3. Check if one set is a subset of another
# #4. Find elements present in the first list but not in the second
# #5.Find all unique vowels in a given string


# #Practice problems on Set
# # 1.Remove duplicates from a list using a set
# numbers = [1, 2, 2, 3, 4, 4, 5]
# unique_numbers = list(set(numbers))
# print("Unique numbers:", unique_numbers)

# #2. Find common elements between two lists using sets
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# common = set(list1) & set(list2)
# print("Common elements:", common)

# #3. Check if one set is a subset of another
# A = {1, 2, 3}
# B = {1, 2, 3, 4, 5}

# print("Is A subset of B?", A.issubset(B))

# #4. Find elements present in the first list but not in the second
# list1 = [10, 20, 30, 40]
# list2 = [30, 40, 50, 60]

# difference = set(list1) - set(list2)
# print("Elements in list1 but not in list2:", difference)

# #5.Find all unique vowels in a given string
# string = "programming in python"
# vowels = {"a", "e", "i", "o", "u"}

# unique_vowels = set(string) & vowels
# print("Unique vowels:", unique_vowels)

