# Series 2 4 6 8 10...N
# print first N even numbers => 2,4,6,8...
print("First even numbers")
N = int(input())
i=1 
k=2
while(i<=N):
    print(k)
    k+=2
    i+=1
# print first N odd numbers => 1,3,5,7....
print("First odd numbers")
N = int(input())
i=1
k=1
while(i<=N):
    print(k)
    k+=2
    i+=1
print # * # * .....N
# print("Print #* pattern ")
N = int(input())
i=1
while(i<=N):
    if(i%2!=0):
        print("# ",end=" ")
    else:
        print("* ",end=" ")
    i+=1
# print # * ## *** ### ****...
print("#**##***...")
N= int(input())
i=1
while(i<=N):
    if(i%2!=0):
        print("#" *i,end="")
    else:
        print("*" *i,end="")
    i+=1
# print 5 10 15 20 25 ....
print("Multiples of 5")
N= int(input())
i=1
while(i<=N):
    print(5*i , end =" ")
    i+=1
# Try above problem with for loop