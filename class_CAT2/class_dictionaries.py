# """
# Dictionaries - key-value pairs, nested dictionaries
# Dictionaries Comprehension

# Dictionaries in Python

# A dictionary is a collection of key-value pairs.

# Defined using {} with key: value.

# Keys must be unique and immutable (e.g., strings, numbers, tuples).

# Values can be any data type (mutable or immutable).
# """
# # Creating a dictionary
# student = {
#     "name": "Alice",
#     "age": 22,
#     "course": "Computer Science"
# }

# print(student["name"])   # Alice
# print(student.get("age")) # 22

# # Key Value Pairs
# student["grade"] = "A"   # Adding new key-value pair
# student["age"] = 23      # Updating value
# print(student)

# del student["course"]    # Deleting key-value
# print(student)

# # Nested Dictionaries
# students = {
#     "101": {"name": "Alice", "age": 22},
#     "102": {"name": "Bob", "age": 23},
#     "103": {"name": "Charlie", "age": 21}
# }

# print(students["102"]["name"])  # Bob

# # Dictinary Comprehension
# # Example 1: Squares of numbers
# squares = {x: x**2 for x in range(1, 6)}
# print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# # Example 2: Convert string to dictionary with char: ASCII value
# ascii_dict = {ch: ord(ch) for ch in "abc"}
# print(ascii_dict)  # {'a': 97, 'b': 98, 'c': 99}
  
# #practice problems on Dictionaries
# # 1.Count frequency of elemnents in a list
# #2. Merge two dictionaries
# #3. Create a dictionary from two lists
# #4. Find the key with the maximum value in a dictionary
# #5. Reverse key-value pairs in a dictionary


# #practice problems on Dictionaries
# # 1.Count frequency of elemnents in a list

# numbers = [1, 2, 2, 3, 4, 4, 4, 5]
# frequency = {}

# for num in numbers:
#     frequency[num] = frequency.get(num, 0) + 1

# print("Frequency:", frequency)

# #2. Merge two dictionaries
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}

# merged = {**dict1, **dict2}
# print("Merged Dictionary:", merged)

# #3. Create a dictionary from two lists
# keys = ["name", "age", "city"]
# values = ["Alice", 25, "Paris"]

# person = dict(zip(keys, values))
# print("Dictionary:", person)

# #4. Find the key with the maximum value in a dictionary
# marks = {"Alice": 85, "Bob": 92, "Charlie": 78}

# max_key = max(marks, key=marks.get)
# print("Top scorer:", max_key, "with marks", marks[max_key])

# #5. Reverse key-value pairs in a dictionary
# original = {"a": 1, "b": 2, "c": 3}
# reversed_dict = {v: k for k, v in original.items()}
# print("Reversed Dictionary:", reversed_dict)

