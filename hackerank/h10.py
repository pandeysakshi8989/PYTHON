# Functions - Perfect Number Detection for Vault Security

def detectPerfectNumber(n: int) -> int:
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i

    if divisors_sum == n:
        return 1
    else:
        return divisors_sum


n = int(input())
print(detectPerfectNumber(n))

# Functions - Calculating the Total of Unique Products Sold

def SumUniqueElements(arr, length):
    freq = {}
    
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    total = sum(num for num in freq if freq[num] == 1)
    
    return total

n = int(input().strip())  
arr = list(map(int, input().split()))  

print(SumUniqueElements(arr, n))

# Functions - Finding the Leaders in Sales Data

def SumOfLeaders(arr, n):
    if not arr or n == 0:  
        return -1
    
    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)  
    
    for i in range(n-2, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]
    
    return sum(leaders)

n = int(input())  
arr = list(map(int, input().split()))  

print(SumOfLeaders(arr, n))

# Functions - Finding the Leaders in Sales Data

def SumOfLeaders(arr, n):
    if not arr or n == 0:  
        return -1
    
    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)  
    
    for i in range(n-2, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]
    
    return sum(leaders)

n = int(input())  
arr = list(map(int, input().split()))  

print(SumOfLeaders(arr, n))

# Functions - Secure Login System Password Validator

def CheckPassword(password: str) -> int:
    n = len(password)
    
    if n < 4:
        return 0
    
    if password[0].isdigit():
        return 0
    
    if not any(ch.isdigit() for ch in password):
        return 0
    
    if not any(ch.isupper() for ch in password):
        return 0
    
    if " " in password or "/" in password:
        return 0
    
    return 1

password = input().strip()
print(CheckPassword(password))

# Functions - Efficient Budget Allocation for Project Expenses

def OddEvenSum(num: int) -> int:
    odd_sum = 0
    even_sum = 0

    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
        num //= 10

    return max(odd_sum, even_sum)

num = int(input())
print(OddEvenSum(num))

# Functions - Secure Login System Password Validator

def CheckPassword(password: str) -> int:
    n = len(password)
    
    if n < 4:
        return 0
    
    if password[0].isdigit():
        return 0
    
    if not any(ch.isdigit() for ch in password):
        return 0
    
    if not any(ch.isupper() for ch in password):
        return 0
    
    if " " in password or "/" in password:
        return 0
    
    return 1

password = input().strip()
print(CheckPassword(password))

# Functions - Efficient Budget Allocation for Project Expenses

def OddEvenSum(num: int) -> int:
    odd_sum = 0
    even_sum = 0

    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
        num //= 10

    return max(odd_sum, even_sum)

num = int(input())
print(OddEvenSum(num))

# Functions - Switching Letters in a Text

def replaceCharacter(s: str, n: int, ch1: str, ch2: str) -> str:
    if not s:   
        return None
    
    if ch1 == ch2:  
        return s

    result = []
    for ch in s:
        if ch == ch1:
            result.append(ch2)
        elif ch == ch2:
            result.append(ch1)
        else:
            result.append(ch)

    return "".join(result)

s = input().strip()
ch1 = input().strip()
ch2 = input().strip()
print(replaceCharacter(s, len(s), ch1, ch2))

# Functions - Matrix Update for Weather Forecast Analysis

def ReplaceDiagonal(mat, m):
    if not mat or m == 0:
        return mat

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]

    for i in range(m):
        total = 0
        for dx, dy in directions:
            ni, nj = i + dx, i + dy  
            if 0 <= ni < m and 0 <= nj < m:
                total += mat[ni][nj]
        mat[i][i] = total

    return mat

m = int(input().strip())
mat = [list(map(int, input().split())) for _ in range(m)]

updated = ReplaceDiagonal(mat, m)

for row in updated:
    print(" ".join(map(str, row)))

# Functions - Water Tank Filling Time Calculation

def TimeToFill(l, b, h, r):
    if r == 0:  
        return 0
    volume = l * b * h
    time_required = volume // r  
    return time_required


l = int(input())
b = int(input())
h = int(input())
r = int(input())

print(TimeToFill(l, b, h, r))

# Functions - Switching Letters in a Text

def replaceCharacter(s: str, n: int, ch1: str, ch2: str) -> str:
    if not s:   
        return None
    
    if ch1 == ch2:  
        return s

    result = []
    for ch in s:
        if ch == ch1:
            result.append(ch2)
        elif ch == ch2:
            result.append(ch1)
        else:
            result.append(ch)

    return "".join(result)

s = input().strip()
ch1 = input().strip()
ch2 = input().strip()
print(replaceCharacter(s, len(s), ch1, ch2))

# Functions - Matrix Update for Weather Forecast Analysis

def ReplaceDiagonal(mat, m):
    if not mat or m == 0:
        return mat

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]

    for i in range(m):
        total = 0
        for dx, dy in directions:
            ni, nj = i + dx, i + dy  
            if 0 <= ni < m and 0 <= nj < m:
                total += mat[ni][nj]
        mat[i][i] = total

    return mat

m = int(input().strip())
mat = [list(map(int, input().split())) for _ in range(m)]

updated = ReplaceDiagonal(mat, m)

for row in updated:
    print(" ".join(map(str, row)))

# Functions - Water Tank Filling Time Calculation

def TimeToFill(l, b, h, r):
    if r == 0:  
        return 0
    volume = l * b * h
    time_required = volume // r  
    return time_required


l = int(input())
b = int(input())
h = int(input())
r = int(input())

print(TimeToFill(l, b, h, r))

# Functions - Finding Divisible Sub-Numbers in a Transaction ID

def divisibilityByEleven(num):
    s = str(num)
    n = len(s)
    count = 0
    
    for i in range(n):             
        for j in range(i+1, n+1):  
            fragment = int(s[i:j])
            if fragment % 11 == 0:
                count += 1
                
    return count

num = int(input())
print(divisibilityByEleven(num))

# Functions - Generating Excel Column Labels

def FindExcelColumnName(n):
    result = []
    
    while n > 0:
        n -= 1  
        remainder = n % 26
        result.append(chr(ord('A') + remainder))
        n //= 26
    
    return ''.join(reversed(result))


n = int(input())
print(FindExcelColumnName(n))


