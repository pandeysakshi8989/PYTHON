# Questions on Sequence data types - lists , tuples, sets, dictionaries
#1.
a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(b)

#2.
lst = [10, 20, 30, 40, 50]
print(lst[1:4])
print(lst[-4:-1])

#3.
lst = [10, 20, 30, 40, 50]
print(lst[1:])
print(lst[:-1])

#4.
t = (1, [2, 3], 4)
t[1].append(5)
print(t)

#5.
s = {1, 2, 2, 3, 4, 4}
print(s)

#6.
d = {1: "A", 2: "B", 1: "C"}
print(d)

#7.
d = {"a": [1, 2], "b": [3, 4]}
d["a"].append(5)
print(d)

#8.
lst = [1, 2, 3, [4, 5]]
print(3 in lst)
print([4, 5] in lst)

#9.
a, b, c = 1, 2, 3
t = a, b, c
print(t)

#10.
d = {frozenset([1, 2]): "Hello"}
print(d[frozenset([1, 2])])

#11.
lst = [[0]] * 3
lst[0][0] = 5
print(lst)

#12.
t = (1, 2, [3, 4])
t[2] += [5, 6]
print(t)

#13.
a = [1, 2, 3]
b = [a, a, a]
b[0][1] = 99
print(b)

#14.
d = {}
d[True] = "Yes"
d[1] = "One"
d[1.0] = "Float"
print(d)

#15.
s = {1, 2, (3, 4)}
print(s)
s.add((5, [6, 7]))

#16.
d = {}
print(d.get("x", []))
d["x"] = d.get("x", [])
d["x"].append(1)
print(d)

#17.
a = {1, 2, 3}
b = {3, 4, 5}
print(a ^ b)

#18.
d = {(1, 2): "A", (1, 2, 3): "B"}
print(d[(1, 2)], d.get((2, 1)))

#19.
print("ab" in ["a", "b", "ab"])
print("a" in {"a": 1, "b": 2})

#20.
d = {[1, 2]: "A"}
print(d)


#  Questions on arrays and strings
# 1.
arr = [[0]] * 3
arr[0].append(1)
print(arr)

#2.
arr = [1, 2, 3, 4]
b = arr[:]
b[0] = 99
print(arr, b)

#3.
from array import array
a = array('i', [1, 2, 3])
b = a
b[0] = 10
print(a, b)

#4.
arr = [[1, 2], [3, 4]]
print(arr[0][1], arr[1][0])

#5.
a = [[0] for i in range(3)]
a[0][0] = 5
print(a)

#6.
s = "hello"
s[0] = "H"
print(s)

#7.
s = "python"
print(s[::-1])
print(s[1:5:2])

#8.
a = "hello"
b = "hello"
print(a is b)

#9.
s = "-".join("ABC")
print(s)

#10.
s = "abc"
print(s*3)
print("".join([s]*3))

#11.
arr = [[1, 2], [3, 4]]
b = arr[:]
b[0][0] = 99
print(arr)

#12.
a = [1, 2, 3]
b = a[:]
print(a == b, a is b)

#13.
a = [1, 2, [3, 4]]
b = a.copy()
b[2][0] = 99
print(a, b)

#14.
a = [[]] * 3
a[1].append(5)
print(a)

#15.
from array import array
arr = array('i', [1, 2, 3, 4, 5])
print(arr[1:4])

#16.
s = "abcdef"
print(s[::-2])

#17.
s = "banana"
s.replace("a", "o")
print(s)

#18.
a = "hello_world"
b = "hello_" + "world"
print(a is b)

#19.
s = "A"
print(ord(s), chr(65))

#20.
s = "python"
print("py" in s, "to" in s, "on" in s)


# Questions on functions and recursion
#1.
def add_to_list(val, lst=[]):
    lst.append(val)
    return lst

print(add_to_list(1))
print(add_to_list(2))

#2.
def outer(x):
    def inner(y):
        return x + y
    return inner

f = outer(5)
print(f(10))

#3.
x = 10
def fun():
    x = 20
    print(x)

fun()
print(x)

#4.
x = 5
def fun():
    global x
    x = 15

fun()
print(x)

#5.
def fact(n, acc=1):
    if n == 0:
        return acc
    return fact(n-1, acc*n)

print(fact(5))

#6.
def rec(n):
    if n == 0:
        return
    print(n, end=" ")
    rec(n-1)

rec(3)

#7.
def even(n):
    if n == 0: return True
    return odd(n-1)

def odd(n):
    if n == 0: return False
    return even(n-1)

print(even(4), odd(4))

#8.
def hello():
    return "Hi"

greet = hello
print(greet(), hello())

#9.
def reverse(s):
    if len(s) == 0:
        return s
    return reverse(s[1:]) + s[0]

print(reverse("abc"))

#10.
def func(a, b, c):
    print(a, b, c)

lst = [1, 2, 3]
func(*lst)

#11.
def f(x, l=[]):
    l.append(x)
    return l

print(f(10))
print(f(20))
print(f(30, []))
print(f(40))

#12.
def rec(n):
    if n == 0:
        return 0
    print(n, end=" ")
    return n + rec(n-1)

print("\nSum:", rec(4))

#13.
def outer(a):
    def inner(b):
        return a * b
    return inner

x = outer(5)
print(x(3))

#14.
fact = (lambda f: (lambda x: f(f, x)))(
            lambda f, n: 1 if n==0 else n*f(f, n-1)
        )

print(fact(5))

#15.
x = 50
def func(x):
    print(x)
    x = 2
    print(x)

func(10)
print(x)

#16.
def is_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

print(is_palindrome("madam"))
print(is_palindrome("hello"))

#17.
def calculator(x):
    def add(y): return x + y
    def mul(y): return x * y
    return add, mul

a, m = calculator(5)
print(a(3), m(3))

#18.
def rec(n):
    if n == 0: return
    rec(n-1)
    print(n, end=" ")

rec(3)

#19.
def square(x): return x*x
def apply(func, val): return func(val)

print(apply(square, 5))

#20.
memo = {}
def fib(n):
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

print(fib(6))

