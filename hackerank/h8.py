# Array 2D 
# P1: Merging Attendance Records
rows, column = map(int, input().split())
matrix = [list(map(int, input().split()))  for _ in range(rows)]
matrix2 = [list(map(int, input().split()))  for _ in range(rows)]

for i in range(rows):
    for j in range(column):
        print(matrix[i][j]+matrix2[i][j],end=" ")
    print()

# P2: Irene's Audience Arrangement Checker
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
is_upper =1
for i in range(n):
    for j in range(i):
        if matrix[i][j]!=0:
            is_upper =0

if(is_upper ==1):
    print("Upper triangular matrix")
else:
    print("Not a triangular matrix")

#P3: Robotic Warehouse Navigation - Snake Pattern Traversal
rows,columns = map(int, input().split())
matrix = [list(map(int,input().split())) for _ in range(rows)]
for i in range(rows):
    if(i%2 == 0):
        for j in range(columns):
            print(matrix[i][j],end = " ")
    else:
        for j in range(columns-1,-1,-1):
            print(matrix[i][j],end = " ")

# P4: Identifying Maximum Defects Levels in Production Batches
rows,columns = map(int, input().split())
matrix = [list(map(int,input().split())) for _ in range(rows)]
for i in range(rows):
        print(max(matrix[i]))

#P5: Counting Sorted Production Lines
rows ,columns = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(rows)]
count = 0
for row in matrix:
    if all(row[i] <= row[i+1] for i in range(columns-1)):
        count+=1
print(count)

#P6: Power Grid Monitoring - Computing Duagonal Load Balanaces
n = int(input())
matrix = [list(map(int, input())) for _ in range(n)]
p_sum =0
s_sum =0
for i in range(n):
    p_sum += matrix[i][i]
    s_sum += matrix[i][n-i-1]
print(p_sum,s_sum)

# P7: Image Rotation Feature
n = int(input())
matrix = [list(map(int, input())) for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for i in range(n):
    matrix[i].reverse()
for row in matrix:
    print(" ".join(map(str,row)))

#P8: Warehouse Inventory Sum
n = int(input().strip())
matrix = [list(map(int, input().split())) for _ in range(n)]

print("Row sums:")
for i in matrix:
    print(sum(i))

print("Columns sums: ")
for j in range(n):
    print(sum(matrix[i][j]) for i in range(n))

#P9: Warehouse Shelf Max Quantity
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for j in range(n):
    max_val =max(matrix[i][j] for i in range(n))
    print(max_val)
