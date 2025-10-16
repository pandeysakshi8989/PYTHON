"""
Exception handling : try, except, else, finally
Built- in  exceptions
Raising exceptions manually
"""
"""

# 🔹 **1. Exception Handling in Python**

* Exceptions are **errors that occur during program execution**.
* If not handled, they stop the program.
* Python provides `try`, `except`, `else`, and `finally` blocks to handle them.

---

## ✅ **Syntax**

```python
try:
    # Code that may raise an exception
except SomeError:
    # Code to handle error
else:
    # Runs if no exception occurs
finally:
    # Runs no matter what (cleanup code)
```

---

# 🔹 **2. Example with try, except, else, finally**

```python
try:
    num = int(input("Enter a number: "))
    print("Square is:", num ** 2)
except ValueError:
    print("Invalid input! Please enter a number.")
else:
    print("Executed successfully without error.")
finally:
    print("Program ended.")
```

---

# 🔹 **3. Built-in Exceptions**

Some common built-in exceptions in Python:

* `ZeroDivisionError` → Division by zero
* `ValueError` → Invalid type conversion
* `TypeError` → Wrong type used
* `IndexError` → Invalid list index
* `KeyError` → Dictionary key not found
* `FileNotFoundError` → File doesn’t exist
* `ImportError` → Importing unavailable module

---

## ✅ Example of Built-in Exceptions

```python
try:
    lst = [1, 2, 3]
    print(lst[5])   # IndexError
except IndexError as e:
    print("Error:", e)
```

---

# 🔹 **4. Raising Exceptions Manually**

You can raise exceptions using `raise`.

```python
age = 15
if age < 18:
    raise ValueError("Age must be at least 18.")
```

---

# 🔹 **5. 10 Practice Problems with Code**

---

## **Q1. Handle division by zero**

```python
try:
    a, b = 5, 0
    print(a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
```

---

## **Q2. Handle invalid integer input**

```python
try:
    num = int("abc")
except ValueError:
    print("Error: Invalid integer conversion.")
```

---

## **Q3. Handle multiple exceptions**

```python
try:
    data = [1, 2, 3]
    print(data[5] / 2)
except IndexError:
    print("Error: Index out of range.")
except ZeroDivisionError:
    print("Error: Division by zero.")
```

---

## **Q4. Use else with exception handling**

```python
try:
    num = 10
    result = num / 2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("Result:", result)
```

---

## **Q5. Use finally for cleanup**

```python
try:
    f = open("sample.txt", "w")
    f.write("Hello World")
except Exception as e:
    print("Error:", e)
finally:
    f.close()
    print("File closed safely.")
```

---

## **Q6. Raise custom exception if negative number is entered**

```python
num = -5
if num < 0:
    raise ValueError("Negative numbers are not allowed.")
```

---

## **Q7. Handle KeyError in dictionary**

```python
try:
    student = {"name": "Alice"}
    print(student["age"])
except KeyError:
    print("Error: Key not found in dictionary.")
```

---

## **Q8. Handle FileNotFoundError**

```python
try:
    f = open("non_existing.txt", "r")
except FileNotFoundError:
    print("Error: File does not exist.")
```

---

## **Q9. Handle TypeError**

```python
try:
    result = "10" + 5
except TypeError:
    print("Error: Cannot add string and integer.")
```

---

## **Q10. Function with exception handling**

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"

print(divide(10, 2))  # 5.0
print(divide(10, 0))  # Error: Division by zero
```

---

✅ **Quick Recap**:

* `try` → risky code
* `except` → handles exception
* `else` → runs if no exception
* `finally` → always runs (cleanup)
* Can handle built-in exceptions (`ValueError`, `IndexError`, etc.)
* Can **raise exceptions manually** with `raise`.

"""