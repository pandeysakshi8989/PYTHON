# Example:
i = 1
while i < 6:
  print(i)
  i += 1
# Example:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
# Example:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
# Example:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


# Example:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
# Example:
for x in "banana":
  print(x)
# Example:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
# Example:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
# Example:
for x in range(6):
  print(x)
#Example:
for x in range(2, 6):
  print(x)
# Example:
for x in range(2, 30, 3):
  print(x)
#Example:
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#Example:
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#Example:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
#Example:
for x in [0, 1, 2]:
  pass
i = 0
while i <10:
  i += 1
  if i %5==0:
    continue
  print(i) #This is corrected code