# Looping
#Looping - Adam’s Charity
N = int(input()) # N=10
# i = 1
sum = 0
for i in range(1, N+1): # 1 to 11-1 =10 => range function plays role for moving from 1 to N+1 
    sum += i * i

print(sum)
    

#Looping - Car Speed
N = int(input())
sum =0 
for i in range(1, N+1):
    if N % i ==0:
        sum += i
print(sum)

# Looping - Next Leap Year
year = int(input()) # representing N for year

while(True):
    if ( (year % 400 ==0) or (year %4 ==0 and year% 100!=0)):
        print(year)
        break
    year+=1


#Looping - Quality Check for Premium Products
N = int(input())
if N <= 1:
    print("Regular Product")
else:
    is_prime = True
    i = 2
    while i * i <= N:   # same as range(2, sqrt(N)+1)
        if N % i == 0:
            is_prime = False
            break
        i += 1
    
    if is_prime:
        print("Premium Product")
    else:
        print("Regular Product")


# Looping - Coding Marathon
N = int(input())        
K = int(input())        
marks = list(map(int, input().split()))  

marks.sort(reverse=True)

result = 0
for i in range(K):
    result += marks[i]

print(result)

#Looping - Optimizing Energy Division for Maximum Efficiency
N = int(input().strip())

if N < 1 or N > 100:
    print("Invalid")
else:
    max_product = 0
    
    for i in range(1, N):  
        j = N - i
        product = i * j

        temp_product = i
        for k in range(j, 0, -3):   # decrease k by 3 each time
            if k > 4:
                temp_product *= 3
            else:
                temp_product *= k
                break

        max_product = max(max_product, product, temp_product)

    print(max_product)

#Looping - Teaching Digit Positions
N = int(input().strip())  
K = int(input().strip())  

num_str = str(N)

digit = -1   
count = 1
i = 0

while i < len(num_str):
    if count == K:
        digit = int(num_str[i])
        break
    count += 1
    i += 1

print(digit)

# Looping - Unique-Digit Numbers for Ticket Validation
n1 = int(input().strip())
n2 = int(input().strip())

if n1 > n2:
    n1, n2 = n2, n1

count = 0

for num in range(n1, n2 + 1):
    digits = str(num)
    seen = set()
    unique = True

    for ch in digits:
        if ch in seen:
            unique = False
            break
        seen.add(ch)

    if unique:
        count += 1

print(count)


#Looping - Inventory Check for Rare Items
n = int(input().strip())
temp = n
sum_fact = 0

for digit in str(temp):
    digit = int(digit)
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    sum_fact += fact

if sum_fact == n:
    print("Rare Item")
else:
    print("Common Item")

# Looping - Calculating Plant Growth Stages
n = int(input().strip())
a, b = 0, 1
for i in range(n + 1):
    print(a, end=" ")
    a, b = b, a + b
