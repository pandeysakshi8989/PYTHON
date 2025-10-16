# """
# Strings
# String functions

# 🔹 1. Strings in Python

# A string is a sequence of characters enclosed in single (' '), double (" "), or triple quotes (''' ''' or """ """).

# Strings are immutable (cannot be changed once created).

# 🔹 2. String Functions

# Python provides many built-in functions and methods to work with strings.

# ✅ Common String Functions with Examples:
# """
# # String creation
s1 = 'Hello'
s2 = "World"
s3 = '''Python Programming'''

print(s1, s2, s3)


s = " Python Programming " # Take your full name apply this functions

print(len(s))             # length → 20
print(s.lower())          # lowercase → ' python programming '
print(s.upper())          # uppercase → ' PYTHON PROGRAMMING '
print(s.strip())          # removes leading/trailing(extra) spaces
print(s.replace("Python", "Java"))  # replace substring # 'Java Programming'

s2 = "hello world"
print(s2.capitalize())    # 'Hello world'
print(s2.title())         # 'Hello World'
print(s2.find("world"))   # index of substring → 6
print(s2.count("l"))      # count occurrences of character → 3
print("123".isdigit())    # True
print("abc".isalpha())    # True
print("abc123".isalnum()) # True
print(",".join(["apple","banana","cherry"]))  # 'apple,banana,cherry'
print("apple,banana".split(","))              # ['apple', 'banana']


# # practice problems
# # Q1. Reverse a string without using slicing
# # Q2. Count vowels in a given string
# # Q3. Check if a string is a palindrome
# # Q4. Find the most frequent character in a string
# # Q5. Remove all special characters from a string

# # Q1. Reverse a string without using slicing
# def reverse_string(s):
#     rev = ""
#     for ch in s:
#         rev = ch + rev
#     return rev

# print(reverse_string("Python"))

# # Q2. Count vowels in a given string
# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     return sum(1 for ch in s if ch in vowels)

# print("Vowels:", count_vowels("Hello World"))

# # Q3. Check if a string is a palindrome
# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("madam"))   # True
# print(is_palindrome("hello"))   # False

# # Q4. Find the most frequent character in a string
# def most_frequent(s):
#     freq = {}
#     for ch in s:
#         freq[ch] = freq.get(ch, 0) + 1
#     return max(freq, key=freq.get)

# print("Most frequent:", most_frequent("mississippi"))

# # Q5. Remove all special characters from a string
# def remove_special(s):
#     return "".join(ch for ch in s if ch.isalnum() or ch.isspace())

# print(remove_special("Hello@123! Python#"))
