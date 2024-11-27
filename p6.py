
friends = ["kevin","karen","jim","jim","oscar","tody"]

print(friends)

print(friends[0])

print(friends[-1])

print(friends[1:3])

friends[1]="mike"
print(friends[1])

lucky_numbers =[ 4,8,15,16,23,42]

print(lucky_numbers)

friends.extend(lucky_numbers)
print(friends)

friends.append("creed")
print(friends)

friends.insert(1,"kelly")
print(friends)

friends.remove("jim")
print(friends)

# friends.clear()
# print(friends)

friends.pop()
print(friends)

print(friends.index("kevin"))

print(friends.count("jim"))

friends.sort()
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)