# """
# Tuples in Python

# A tuple is an ordered, immutable collection in Python.

# Defined using ()` (parentheses).

# Allows duplicates.

# Can store different data type

# Tuples - unpacking, immutability

# """
# # Tuples
# # Creating a tuple
# my_tuple = (10, 20, 30, "hello", 3.14)
# print(my_tuple)

# # Tuple unpacking
# # Tuple unpacking
# person = ("Alice", 25, "Engineer")

# name, age, profession = person

# print("Name:", name)
# print("Age:", age)
# print("Profession:", profession)

# # to gather extra value use *
# numbers = (1, 2, 3, 4, 5)

# a, b, *rest = numbers
# print(a, b)      # 1 2
# print(rest)      # [3, 4, 5]

# # Tuple Immutability
# my_tuple = (10, 20, 30)

# # Trying to change a value
# # my_tuple[1] = 99   ❌ This will raise an error

# print(my_tuple)  # (10, 20, 30)

# #create new tuple
# my_tuple = (10, 20, 30)
# new_tuple = my_tuple + (40, 50)

# print(new_tuple)  # (10, 20, 30, 40, 50)

# #Tuples with Nested Mutable Elements

# nested_tuple = (1, [2, 3, 4], 5)

# nested_tuple[1][0] = 99   # modifying the list inside tuple

# print(nested_tuple)  # (1, [99, 3, 4], 5)

# # Practice problemson Tuples 
# #Q1. Create a tuple of 4 values and unpack them
# #Q2. Swap two numbers using tuple unpacking
# #Q3 Try modifying a tuple element
# #Q4 Tuple with a list inside it
# #Q5 Concatenate two tuples

# # Practice problemson Tuples 
# #Q1. Create a tuple of 4 values and unpack them
# # Creating a tuple
# person = ("Alice", 25, "New York", "Engineer")

# # Tuple unpacking
# name, age, city, profession = person

# print("Name:", name)
# print("Age:", age)
# print("City:", city)
# print("Profession:", profession)

# #Q2. Swap two numbers using tuple unpacking
# a = 10
# b = 20

# print("Before Swap: a =", a, ", b =", b)

# # Swapping using tuple unpacking
# a, b = b, a

# print("After Swap: a =", a, ", b =", b)

# #Q3 Try modifying a tuple element
# my_tuple = (1, 2, 3, 4)

# # Trying to modify (this will cause error)
# try:
#     my_tuple[1] = 99
# except TypeError as e:
#     print("Error:", e)

# #Q4 Tuple with a list inside it
# nested_tuple = (1, [2, 3, 4], 5)

# print("Before modification:", nested_tuple)

# # Modifying the list inside the tuple
# nested_tuple[1][0] = 99

# print("After modification:", nested_tuple)

# #Q5 Concatenate two tuples
# tuple1 = (10, 20, 30)
# tuple2 = ("A", "B", "C")

# # Concatenation
# new_tuple = tuple1 + tuple2

# print("Concatenated Tuple:", new_tuple)
