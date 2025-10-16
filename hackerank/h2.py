# Operators
# Operators - Fencing and Carpet Calculation for a Fighting Ground
l = int(input())
b = int(input())
peri = 2 *(l+b)
area = l*b
print(f"The required length is {peri} m")
print(f"The required area of carpet is {area} sqm")

# Operators - Store water
R = int(input())
H = int(input())
import math
water = round(3.14 * R * R *H)
print(water)

# Operators - Fitness App
# minutes into seconds
# 1 minute = 60 second
# minute * 60 -> seconds

N = int(input()) # N is representing minutes
S = N * 60 # S is representing seconds
print(S)

# Operators - The Clock System
X = int(input())
Y = int(input())
product = X * Y
result = product % 12
if result == 0:
    result = 12
print(result)
        
# Operators - Profit Calculation for The Herald Newspaper
copies = int(input())
rate = int(input())
cost = int(input())
revenue = copies * rate
cost = copies * cost + 100
profit = revenue -cost
print(profit)

# Operators - Opening the Enchanted Door
n = int(input())

if 1000 <= n <= 9999:   # check if it's a four-digit number
    first = n // 1000   # extract first digit
    last = n % 10       # extract last digit
    print(first + last)
else:
    print("Lock")

# Operators - Team Games with Ross Geller
friends = int(input())
team = int(input())
num = friends // team
left = friends % team
print(f"The number of friends in each team is {num} and left out is {left}")

# Operators - Goal Tracker
S = int(input())
D = int(input())
N = int(input())
import math
print(round((S-D)/N))

# Operators - Leena's Business Loan
# Input values
X = float(input())  # Principal
R = float(input())  # Rate of interest
Y = float(input())  # Loan period (years)

# Calculations
interest = (X * R * Y) / 100
total_amount = X + interest
discount = 0.02 * interest
final_amount = total_amount - discount

# Output with 2 decimal formatting
print(f"Interest: {interest:.2f}")
print(f"Total Amount: {total_amount:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final Settlement Amount: {final_amount:.2f}")

#Operators - Currency Conversion Helper for Kamal
dollar1 = int(input())
cent1   = int(input())
dollar2 = int(input())
cent2   = int(input())

total_dollars = dollar1 + dollar2
total_cents   = cent1 + cent2

if total_cents >= 100:
    extra_dollars = total_cents // 100
    total_dollars += extra_dollars
    total_cents = total_cents % 100

print(total_dollars)
print(total_cents)
