
# Bitwise Opeartors

a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

# Ternary operators
a, b = 10, 20
min = a if a < b else b

print(min)

# Identity Operators
a = 10
b = 20
c = a

print(a is not b)
print(a is c)

# Membership Operators
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")



"""
Operator 	Meaning	Associativity 
( )	Parentheses  	left-to-right
**	Exponent	right-to-left
*  /  %	Multiplication/division/modulus	left-to-right
+  -	Addition/subtraction	left-to-right
<<  >>	Bitwise shift left, Bitwise shift right	left-to-right
<  <= 	Relational less than/less than or equal to 	left-to-right
>  >=	Relational greater than/greater  than or equal to	Any format
==  !=	Relational is equal to/is not equal to	left-to-right

"""


# Operator Precedence

expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")

# Operator associativity

print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)


