# 1  512
print(2 ** 3 ** 2)
#2  2 2.5
print(5 // 2, 5 / 2)
#3 -3
print(-5//2)
#4 1,2
print(7 % -3, -7 % 3)
#5 1
x = True + True * False
print(x)
#6 8 2
print(2 << 2, 8 >> 2)
#7 2 7
print(3 & 6, 3 | 6)
#8 20
x = 10
x += x - (x % 3)
print(x)
# 9 False, False, False,True
not(True and False)
(not True) or False
not (True or False)
not(False)
#10 **
# which has highest precedence
# *, **, % ,//

# Decision Making
#1 B
x = 5
if x > 5:
    print("A")
elif x == 5:
    print("B")
else:
    print("C")
#2 B
x = 10
if x > 10:
    print("A")
elif x >= 10:
    print("B")
else:
    print("C")
#3 B
x = 0
if x:
    print("A")
else:
    print("B")
#4 True
x = -1
if x:
    print("True Block")
else:
    print("False Block")
#5 C
x = 5
y = 10
if x > y:
    if x > 0:
        print("A")
    else:
        print("B")
else:
    print("C")
#6 B
if False:
    print("A")
elif True:
    print("B")
elif True:
    print("C")
else:
    print("D")
#7 A
x = 15
if x % 3 == 0:
    if x % 5 == 0:
        print("A")
    else:
        print("B")
else:
    print("C")
#8 End
x = 10
if x > 5:
    pass
print("End")
#9 A B
x = 20
if x > 10:
    print("A", end=" ")
if x > 15:
    print("B", end=" ")
if x > 25:
    print("C", end=" ")
#10 Valid
x = 5
if 1 < x < 10:
    print("Valid")
else:
    print("Invalid")


#Looping statements
#1 0 1 2
for i in range(3):
    print(i, end=" ")
#2 0 1 2
i = 0
while i < 3:
    print(i, end=" ")
    i += 1
#3 1 4 7
for i in range(1, 10, 3):
    print(i, end=" ")
#4 0 1 2
for i in range(5):
    if i == 3:
        break
    print(i, end=" ")
#5 0 1 2 4
for i in range(5):
    if i == 3:
        continue
    print(i, end=" ")

#6 1 2 4 5 
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x, end=" ")
#7 0 0; 0 1; 1 0; 1 1; 
for i in range(2):
    for j in range(2):
        print(i, j, end="; ")
#8 0 1 2 Done
for i in range(3):
    print(i, end=" ")
else:
    print("Done")
# 9 prints nothing
for i in range(3):
    if i == 1:
        break
else:
    print("No break")
#10 1 0 -1 -2
i = 1
while i < 5:
    print(i, end=" ")
    i -= 1
    if i == -3:
        break
