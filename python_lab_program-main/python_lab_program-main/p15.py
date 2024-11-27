#Program 15 Use of mebership operators
# initialized some sequences
list1 = [1, 2, 3, 4, 5]
str1 = "Hello World"

# using membership 'in' operator
# checking an integer in a list
print(2 in list1)

# checking a character in a string
print('O' in str1)

# Python program to illustrate the use
# of 'is' identity operator
num1 = 5
num2 = 5

lst1 = [1, 2, 3]
lst2 = [1, 2, 3]

# using 'is' identity operator on different datatypes
print(num1 is num2)
print(lst1 is lst2)