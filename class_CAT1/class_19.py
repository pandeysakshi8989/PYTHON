# fareheit into celsius
faren=float(input("Enter temperature: "))
celsius=(faren-32)*(5/9)
print("celsius:",celsius)

a =int(input())
b =int(input())
result = a +b
print(result)
result = a -b
print(result)
result = a *b
print(result)
result = a /b
print(result)

#swapping variable with and without using third variable
a= 17
b = 15
# temp =0
print(a) # 17
print(b) #15
print("After:")
# a=b #  a =15
# b=temp # 17
a = a- b # a = 17-15 =2
b = a +b # b = 2 + 15 = 17
a= b-a  # a = 17 -2 =15
print(a)
print(b)


# Comparison operators always gives answers as True or False
# >, <, >=, <=, ==, !=

a = 56
b= 78
c= 56
print(a>b)  # False ; 56>78
print(a<b) # True ; 56<78
print(a>=c) # 56 >=56 ; True
print(a<=c) # 56 <=56 ; True
print(a==c) # 56==56 ; True
print(a!=b) # 56!=78 ; True 
# Try for values (34, 32, 67)

# 1. Take a number and check if it is not equal to 100.
# Take a variable and take value through input()
# Take another variable and store value of 100 in it.
# Compare both variable with not equal to opeartor.
# 2. Take a number and check if it's greater than 50.

# Logical opeartors
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

a = 6
b= 1
c= 0
d= ""
print( a and b) #  # when both values are true, then and returns second value
print(a and c) # #when any value is false it will return false value
print(c and a) # #
print( c and d) # #when both values are false values, then returns first false value


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







