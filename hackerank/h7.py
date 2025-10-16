# Arrays 1D
#Arrays 1D - Insertion of New Product IDs
n= int(input())
list1 = list(map(int,input().split()))
new_element = int(input())

pos =0
while True:
    if pos < n and list1[pos] < new_element:
        pos+=1
    else:
        break
list1.insert(pos,new_element)
print(*list1)

# Arrays 1D - Second Occurrence
n = int(input())
list1 = list(map(int,input().split()))
unique_sorted_list = sorted(set(list1))
if len(unique_sorted_list) < 2:
    print(0)
else:
    second_largest = unique_sorted_list[-2]
    print(list1.count(second_largest))

#Arrays 1D - Dinner Dishes
n = int(input())
list1 = list(map(int,input().split()))
if len(list1) <2:
    print(0)
else:
    list1.sort(reverse = True)
    print(list1[0]+list1[1])

#Arrays 1D - Nick's check
n = int(input())
list1 = list(map(int, input().split()))
list1.sort()
is_consecutive = True
for i in range(1,len(list1)):
    if list1[i] != (list1[i-1]+1):
        is_consecutive = False
        break
if is_consecutive == True:
    print(1)
else:
    print(0)

#Arrays 1D - The lost Digit
import array
n = int(input())
array1 = array.array('i',map(int,input().split()))
sum_n = (n * (n+1))//2
sum_a = sum(array1)
miss_n = sum_n - sum_a
print(miss_n)    

#Arrays 1D - Alice's Magical shoes!
n = int(input())
list1 = list(map(int,input().split()))
count =0
for i in range(len(list1)):
    if list1[i] %3 ==0:
        count+=1
print(count)

# Arrays 1D - Data Recovery - Reversing the Sensor Log
n = int(input()) # number of elements 
list1 =  list(map(int, input().split())) # map function for taking more than one input in one line 
# import array 
#array1 = array.array('i',map(int,input().split()))
list1.reverse()
# array1.reverse()
# print(list1) => [27,28,30]
print(*list1) # unpack list elements 27,28,30

#Arrays 1D - Playing with Numbers
n = int(input())
list1 = list(map(int,input().split()))
rotate = int(input())
rotate = rotate % len(list1)
rotated_list = list1[rotate: ]+ list1[:rotate]
print(*rotated_list)

# Arrays 1D - Unsold Products
n =int(input())
list1 = list(map(int, input().split()))
list2 = []
for i in list1:
    if i != 0:
        list2.append(i)
count = list1.count(0)
list2.extend([0] * count)
print(*list2)

#Arrays 1D - Finding the Median of Positive Product IDs
n = int(input())
list1 = list(map(int, input().split()))
list2 = []
for i in list1:
    if i > 0:
        list2.append(i)
if len(list2) < 1:
    print(-1)
else: 
    mid = len(list2) //2
    print(list2[mid])
