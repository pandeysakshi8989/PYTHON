# Swap variables with and without using third variables
# Calculator with input and output performing arithmetic
# Convert farenheit into celsius

a= 15
b= 17
a =17
b =15

a= 17
b =15
print( " a :", a)
print(" b : ",b)
# temp = a
# a= b
# b = temp
print(" After change: ")
# print("a: ",a)
# print("b:",b)

a = a-b # a = 17-15 =2
b = a + b # b = 2 + 15 = 17
a = b- a # a = 17 - 2 = 15

print("a:",a)
print("b:",b)

#FORMULA FOR CONVERSION CELSIUS INTO FAREHEIT
#C = (F- 32) * 5/9

a = int(input())
b = int(input())
result= 0

print("Addition")
result= a +b
print(" Result: ",result)
print("Subtraction")
result= a -b
print(" Result: ",result)
result = a %b
print("Result: ",result)

a = 10
a += 5
print(a)
# ASSIGNMENT OPERATORS WHEN YOU WANT DO OPERATIONS ON SAME VARIABLE ITSELF

# # COMPARISON OPERATORS
# # LOGICAL OPERATORS

a= 56
b=34
print( a > b)
print( a >= b)
print(a < b)
print(a <= b)
print(a == b) # this gives true when values are equal
print(a!=b) # this gives true when values are not equal

# # Try values ( 56, 78), (56,56), (78,56)

# LOGICAL OPERATORS
# AND - GIVES TRUE WHEN BOTH VALUES ARE TRUE, OTHERWISE FALSE
# OR - GIVES TRUE WHEN ANY ONE VALUE IS TRUE, OTHERWISE FALSE
# NOT - GIVES OPPOSITE, LIKE IF TRUE VALUE THEN FALSE, IF FALSE VALUE THEN TRUE
# 0 , "", FALSE ARE CONSIDERED AS FALSE
# 1, TRUE, "GHSGD" , ARE CONSIDERED AS TRUE
# true this will not work,..because,... inpython  only caps True AND False works

a= True
b= True
c= False
d= False
print( a and b)
print(a and c)
print(c and a)
print( c and d)

a = 1
b= 6
c= ""
d= 0
print( a and b) # when both values are true, then and returns second value
print(a and c) # when any value is false it will return false value
print(c and a)
print( c and d) # when both values are false values, then returns first false value


a= True
b= True
c= False
d= False
print( a or b) # or operator gives false when both values are false,
print(a or c) # otherwise or operator gives true
print(c or a)
print( c or d)

a = 1
b= 6
c= ""
d= 0
print( a or b) # when both values are true, then and returns first value
print(a or c) # when any value is true it will return true value
print(c or a)
print( c or d) # when both values are false values, then returns second false value

a= True
b= False
print(not a)
print(not b)

#Comparison Operators

a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# Try with values (23,23), (23, 25), (25,23)

# Logical Operators

a = True
b = False
c= True
d= False

print(a and c)
print(a and b)
print(d and a)
print (b and d)

print(a or c)
print(a or b)
print(d or a)
print (b or d)

print(not a)
print(not b)

a= 1
b=0
c= 6
d= ""

print(a and c)
print(a and b)
print(d and a)
print (b and d)

print(a or c)
print(a or b)
print(d or a)
print (b or d)

print(not a)
print(not b)




