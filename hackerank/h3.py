# Decision making
# Decision Making - Temperature Check for Outdoor Activities
temp = int(input())
if(temp > 0):
    print("Safe for outdoor activities")
else:
    print("Too cold for outdoor activities")

# Decision Making - Event Scheduling for Leap Year Celebrations
year = int(input())
if( (year % 400 ==0 ) or (year % 4 ==0 and year %100 !=0)):
    print("Schedule Event")
else:
    print("No Event This Year")

# Decision Making - Narnian Alphabet Helper
# Program to check if input character is vowel, consonant or not an alphabet

ch = input().strip()

# Check if it's a single alphabet character
if len(ch) == 1 and ch.isalpha():
    # Use a string instead of a list for vowels
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")

# Decision Making - Rock, Paper, Scissors
M = input()

# A -> rock, B->Paper
# A ->scissors , B->Rock
# A -> paper, B -> Scissors

if( M == "rock"):
    print("Paper")
elif(M == "scissors"):
    print("Rock")
elif(M == "paper"):
    print("Scissors")
else:
    print("Invalid input")

# Decision Making - Joey's Quest for the Trendy Meatball Sandwich
n = int(input())

x= abs(n)

if(100 <= x <= 999 ):
    mid = (x//10) % 10
    if(mid % 3 ==0):
        print("Trendy Number")
    else:
        print("Not a Trendy Number")
else:
    print("Invalid Number")

# Decision Making - Car Rental Charges for a Travel Agency
# Taking all inputs
R_f = int(input())# rate of first hours
F_hours = int(input())# number of first hours on which above rate applied
R_a = int(input()) # rate of additional hours
T_m = int(input()) # total number of minutes of travelling
# Calculate total hours by dividing by 60
import math
T_hours = math.ceil(T_m/60) 
# Calculate additional hours
A_hours = T_hours - F_hours  # difference of total hours and total first hours
# Calculate total cost by additing both types of hours  cost
Total_cost = (R_f * F_hours) + (R_a * A_hours)
#Display the total cost as output
print(Total_cost)

# Decision Making - Choosing the Tallest Skyscraper
# Program to find the tallest skyscraper

# Taking three integers as input in one line
h1, h2, h3 = map(int, input().split())

# Find tallest
#tallest = max(h1, h2, h3)

if(h1 >= h2 and h1>=h3):
    tallest =h1
elif(h2>=h3):
    tallest = h2
else:
    tallest = h3

# Print result
print(tallest)

# Decision Making - Selecting the Second Best Candidate
s1,s2,s3=map(int,input().split())
highest = max(s1,s2,s3)
if(s1==highest):
    higher = max(s2,s3)
elif(s2==highest):
    higher = max(s1,s3)
else:
    higher = max(s1,s2)
print(higher)

# Decision Making - Calculating Daily Profit or Loss Percentage
invest = int(input())
earning = int(input())
if(invest >0 and earning >0):
    if(earning > invest):
        profit = int(((earning - invest)/invest)  * 100)
        print(f"Profit - {profit}%" )
    elif(earning < invest):
        loss = int(((invest - earning)/invest)  * 100 )
        print(f"Loss - {loss}%" )
    else:
        print("No Profit, No Loss")
else:
    print("Invalid Input")

# Decision Making - Movie Ticket Price Calculator
age = int(input())
hour = float(input())
if(hour > 0.00 and hour < 24.00):
    if(hour == 13.30):
        price = 2.00
    else:
        if(age > 13):
            price = 5.00
        else:
            price = 2.00
    print(f"${price:.2f}")
else:
    print("Invalid Input")