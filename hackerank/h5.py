# Series - Virus Growth Prediction
n = int(input())
term = 0.5
for i in range(n):
    print(term, end = " ")
    term *=3

# Series - Cricket Run Rate Tracker
n = int(input())
term = 95.0
for i in range(n):
    print(term, end=" ")
    term+=20.5

# Series - Virus Growth Rate Prediction Based on Daily Increases
n = int(input())
term =2
for i in range(n):
    term +=i * 13
    print(term, end=" ")

# Series - Farmer’s Land Expansion
n = int(input())
term =4
for i in range(n):
    term+= i*i
    print(term, end=" ")

# Series - Growth Pattern of the Special Snake
n = int(input())
for i in range(1,n+1):
    print(i*i,end=" " )

# Series - Oranges from the Growing Tree
n = int(input())
term = 6
for i in range(n):
    term+= 5*i
    print(term, end=" ")

# Series - Number Transformation Challenge for Game Development
n = int(input()) # number of terms
print(n, end=" ") # by default print take new line as end
while True:
    if(n ==1):
        break
    if ( n% 2==0): # checking number is even
        n=n//2
        print(n, end=" ") # by default print take new line as end
    else:
        n=n*3+1
        print(n, end=" ") # by default print take new line as end

#Series - Data Compression Simulation
a,r,n = map(int,input().split())
#print( *[a * r**i for i in range(n)])

for i in range(n):
    print(* [a * r**i], end=" ")

# Series - Predictive Analytics for Population Growth
n= int(input())
series = [1,3,4]
if(n<=3 ):
    print(*series[:n])
else:
    for i in range(3,n):
        series.append(series[-1]+ series[-2]+series[-3])
    print(*series)

# Series - Even-Odd Number Arrangement System
n = int(input().strip())
for i in range(1, n+1):
    if i % 2 == 1:  
        print(i+1, end=" ")
    else:           
        print(i-1, end=" ")
