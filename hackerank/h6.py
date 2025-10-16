# # Pattern
# #P1:Pattern - Building a Digital Staircase for a Smart Home System
# n = int(input())
# for i in range(1,n+1):
#     for j in range(1, i+1):
#         print("*",end=" ")
#     print()

# #P2: Pattern - Satge Lighting Arrangement for a Theatre Performance
# n = int(input())
# for i in range(1,n+1):
#     for k in range(n-i,0,-1):
#         print("  ",end="")
#     for j in range(i):
#         print("* ",end="")
#     print()
# #P3: Pattern - Designing a Grand Wedding Hall Ceiling with Chandeliers
# n =int(input())
# for i in range(0,n):
#     for k in range(n-i-1,0,-1):
#         print(" ",end="")
#     for j in range(0,(2*i)+1,1):
#         print("* ",end="")
#     print()
# #P4: Pattern - Stacking Boxes in a Warehouse
n = int(input())
for i in range(n,0,-1):
    print("* "* i)

# #P5:Pattern - Audience Arrangement in a Concert Hall
# n = int(input())
# for i in range(n,0,-1):
#     print("  " *(n-i) + "* "* i )

# #P6: Pattern - Designing a Diamond Pattern of Lights
n = int(input())
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print("  " * (n - i) + "* " * (2 * i - 1))


# #P7:Pattern - Designing an artistic Hourglass Sand dTimer Display
# n = int(input())
# for i in range(n,0,-1):
#     print("  "* (n-i),end="")
#     print("* " * (2*i-1))
# for i in range(1,n,1):
#     print("  "*(n-i-1),end="")
#     print("* "*(2*i+1))

# #P8:Pattern - Designing a Hollow Square Frame for an art Exhibit
# n = int(input())
# for i in range(1, n+1,1):
#     if(i==1 or i==n):
#         print("*" * n)
#     else:
#        print("*"+ " "*(n-2)+"*")
# n = int(input())

# #P9: Pattern - Number Pyramid Pattern with Increasing Digits 
# n = int(input())
# k=1
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         print(k,end="")
#         k+=1
#     print()

# # P10: Decremental pyramid Pattern
# n = int(input())
# start = n * (n+1) //2
# for i in range(n,0,-1):
#     for j in range(i):
#         print(start, end="*" if j<i-1 else "")
#         start-=1
#     print()

# # P10:
# n = int(input())
# s_num = n * (n+1) //2
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         if(j==1):
#             print(f"{s_num}",end="")
#         else:
#             print(f"{s_num}*",end="")
#         s_num-=1
#     print()