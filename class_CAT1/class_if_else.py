"""
REAL WORD APPLICATION OF DECISION MAKING STATEMENTS
1. Banking & Finance
ATM Machines:
If PIN is correct → grant access
Else → deny and show error
Loan Approval:
If credit score > threshold → approve loan
Else → reject or ask for collateral
2. E-commerce & Online Platforms
Discount Application:
If cart value > $100 → apply discount
Else → no discount
Product Recommendation:
If user browsed electronics → show related gadgets
Else → show general products
3. Healthcare
Patient Diagnosis System:
If temperature > 38°C → flag fever
Else → normal status
Medicine Dosing:
If patient age < 12 → give half dose
Else → full dose
4. Transportation
Traffic Lights:
If signal is red → stop
Else if yellow → slow down
Else (green) → go
Airline Check-in:
If baggage weight ≤ allowed limit → proceed
Else → charge extra fee
5. Cybersecurity
Login Authentication:
If username & password match → grant access
Else → deny entry
Fraud Detection:
If transaction > daily limit → block & alert
Else → process normally
6. Smart Devices & IoT
Smart Thermostat:
If temperature < 20°C → turn on heater
Else if temperature > 26°C → turn on AC
Voice Assistant:
If command contains "play music" → open music app
Else if "set alarm" → create alarm
7. Education & Exams
Grading System:
If score ≥ 90 → grade A
Else if ≥ 75 → grade B
Else → fail
Attendance System:
If student present → mark P
Else → mark A
8. Gaming
Character Health:
If health ≤ 0 → game over
Else → continue playing
Reward System:
If player completes level → unlock next stage
Else → retry
"""

"""
# Decision Making

if statement is the most simple decision-making statement.
If the condition evaluates to True, the block of code inside the if statement is executed.

if...else statement is a control statement that helps in decision-making based on specific conditions. 
When the if condition is False. If the condition in the if statement is not true, the else block will be executed.

"""

#Example Code 1: if
i = 10
# Checking if i is greater than 15
if (i > 15):
    print("10 is less than 15")
    
print("I am Not in if")

# Example Code 2: if-else
i = 20
# Checking if i is greater than 0
if (i > 0):
    print("i is positive")
else:
    print("i is 0 or Negative")

    
# Example Code 3: one - line if else
a = -2
# Ternary conditional to check if number is positive or negative
res = "Positive" if a >= 0 else "Negative"
print(res)

# Example Code 4: Logical Operator with if -else
age = 25
exp = 10
# Using '>' operator & 'and' with if-else
if age > 23 and exp > 8:
    print("Eligible.")
else:
    print("Not eligible.")
   
# Example Code 5: Nested If -else
i = 10
if (i == 10):
    #  First if statement
    if (i < 15):
        print("i is smaller than 15")   
    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")        
else:
  print("i is not equal to 10")

# Example Code 6: if-elif-else
i = 25
# Checking if i is equal to 10
if (i == 10):
    print("i is 10")
 # Checking if i is equal to 15
elif (i == 15):
    print("i is 15")
# Checking if i is equal to 20
elif (i == 20):
    print("i is 20")    
# If none of the above conditions are true
else:
    print("i is not present")
