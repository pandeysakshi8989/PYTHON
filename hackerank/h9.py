# Strings

#P10 in 8th sheet:
s = input()    
n = int(input())        
c = input()      
print(s.count(c))

# 9th sheet
#P1: Strings - Lowercase Count
s= input()
n = int(input())
lowercase_letters = ''.join(ch for ch in s if ch.islower())
print(lowercase_letters, len(lowercase_letters))

#P2: Strings - Fanny Occurence
s=input()
x = input()
print(s.replace(x,""))

#P3: Kindergarten Sentene Building
sentence = input()
print(max(len(word) for word in sentence.split()))

#P4: Seat allocation Check for Graduation Ceremony
arrangement = input()
count =0
for i, ch in enumerate(arrangement):
    if ch.lower() == chr(ord('a' + i)):
        count+=1
print(count)
#Second way
arrangement = input()
count = sum(1 for i, ch in enumerate(arrangement) if ch.lower() == chr(97 + i))
print(count)

#P5: Strings - Character Count1
word = input()
print(max(word.count(ch) for ch in set(word)))

#P6: Strings - Data Compression for Server Log Optimization
s = input()
compressed = ''.join(ch for i, ch in enumerate(s) if i == 0 or s[i] != s[i-1])
print(compressed[::-1])


#P7: Strings - Reversing Words for a Speech Teleprometer
s = input()
print(' '.join(s.split()[::-1]))


#P8: Strings - Analyzing Sentence Complexity in Content Writing
s = input().strip()
if not s:
    print(0)
else:
    vowels = "aeiou"
    hard = easy = 0
    for w in s.split():
        v = sum(ch in vowels for ch in w)
        c = sum(ch.isalpha() and ch not in vowels for ch in w)
        max_consec = max((len(x) for x in ''.join('*' if ch not in vowels and ch.isalpha() else ' ' for ch in w).split()), default=0)
        if c > v or max_consec >= 3:
            hard += 1
        else:
            easy += 1
    print(5 * hard - 2 * easy)

# second way
s = input()
if not s:
    print(0)
else:
    vowels = "aeiou"
    hard = easy = 0

    for word in s.split():
        v_count = sum(1 for ch in word if ch in vowels)
        c_count = sum(1 for ch in word if ch.isalpha() and ch not in vowels)

        max_consec = 0
        consec = 0
        for ch in word:
            if ch.isalpha() and ch not in vowels:
                consec += 1
                max_consec = max(max_consec, consec)
            else:
                consec = 0

        if c_count > v_count or max_consec >= 3:
            hard += 1
        else:
            easy += 1

    difficulty = (5 * hard) - (2 * easy)
    print(difficulty)

#P9:Strings - Analyzing Alphanumeric Characters in Official Documents
s = input().strip()
print(-1 if not s else sum(ch.isalnum() for ch in s))

