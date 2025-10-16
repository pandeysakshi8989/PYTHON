# Built -in functions
# Function that helps in doing some actions 
# function_name()
# input()	Allowing user input
# int()	Returns an integer number
# float()	Returns a floating point number
# str()	Returns a string object
# print()	Prints to the standard output device
# The chr() function returns the character that represents the specified unicode.
x = chr(65)
print(x)
# # The ord() function returns the number representing the unicode code of a specified character.
x = ord("H")
print(x)
# #The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
x = round(5.76443, 2)
print(x)
# # The min() and max() functions can be used to find the lowest or highest value in an iterable:
x = min(5, 10, 25, 2)
y = max(5, 10, 25,35)
print(x)
print(y)
# # The abs() function returns the absolute (positive) value of the specified number:
x = abs(-7.25)
print(x)
# # The pow(x, y) function returns the value of x to the power of y (xy).
x = pow(4, 3) # 4 * 4 * 4
print(x) 
y = 4 ** 3
print(y)


# # Python has also a built-in module called math, which extends the list of mathematical functions.
# # The math.sqrt() method for example, returns the square root of a number:
import math
x = math.sqrt(64)
print(x)
# 8 *8 =64
x = math.sqrt(4.25)
print(x)
# #The math.ceil() method rounds a number upwards to its nearest integer,
# #the math.floor() method rounds a number downwards to its nearest integer, and returns the result:
x = math.ceil(1.4) # 2
y = math.floor(1.4) # 1
print(x)  # 1 < 1.4 < 2
print(y) # always gives float value 
# # The math.pi constant, returns the value of PI (3.14...)
x = math.pi
print(x) # pi is used for calculating perimeter and area of circle, cylinder etc.
radius = 5.2
area = x * radius * radius
print(radius)
print(area)
# #The math.trunc() method returns the truncated integer part of a number.
print(math.trunc(2.77))
print(math.trunc(3.37))
