
try:
    answer = 10/5
    number = int(input("Enter a number: "))
    print(number)
    print(answer)
except ZeroDivisionError as err: 
    print("Divided by zero")
except ValueError:
    print("Invalid input")

