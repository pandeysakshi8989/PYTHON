# Example
from __future__ import print_function
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()
# Example
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)
# Example
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break
print('Current Letter :', letter)
# Example
for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)
# Example
fruits = ["apple", "orange", "kiwi"]
for fruit in fruits:
    print(fruit)
# Example
fruits = ["apple", "orange", "kiwi"]
iter_obj = iter(fruits)
while True:
    try:
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
        break



# Example
n = 4
for i in range(0, n):
    print(i)
# Example
li = ["geeks", "for", "geeks"]
for i in li:
    print(i)
# Example   
tup = ("geeks", "for", "geeks")
for i in tup:
    print(i)
# Example    
s = "Geeks"
for i in s:
    print(i)
# Example   
d = dict({'x':123, 'y':354})
for i in d:
    print("%s  %d" % (i, d[i]))
# Example    
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i),
# Example
li = ["geeks", "for", "geeks"]
for index in range(len(li)):
    print(li[index])
# Example
li = ["geeks", "for", "geeks"]
for index in range(len(li)):
    print(li[index])
else:
    print("Inside Else Block")
# Example
cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")
# Example
cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")
else:
    print("In Else Block")
# Example
while (True):
    print("Hello Geek")
