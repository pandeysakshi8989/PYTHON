"""
Files - open(), read, write, append modes
Reading and writing to text files
File methods - read(), readlines(), write()

CSV file operations using csv module

"""

"""

# 🔹 **1. File Handling in Python**

Files are opened in Python using the built-in **`open()`** function.

### **File Modes**

* `"r"` → Read (default mode)
* `"w"` → Write (creates new file or overwrites existing)
* `"a"` → Append (adds to end of file)
* `"r+"` → Read and write
* `"b"` → Binary mode (e.g., `"rb"`, `"wb"`)

---

# 🔹 **2. Opening and Reading a File**

```python
f = open("sample.txt", "r")
content = f.read()        # Read entire file
print(content)
f.close()
```

👉 Use `readline()` for one line, `readlines()` for all lines as a list.

---

# 🔹 **3. Writing to a File**

```python
f = open("sample.txt", "w")   # Overwrites existing content
f.write("Hello, Python!\n")
f.write("File handling example.")
f.close()
```

---

# 🔹 **4. Appending to a File**

```python
f = open("sample.txt", "a")
f.write("\nThis is an appended line.")
f.close()
```

---

# 🔹 **5. Using `with` Statement (Best Practice)**

Automatically closes file after use.

```python
with open("sample.txt", "r") as f:
    print(f.read())
```

---

# 🔹 **6. CSV File Operations (`csv` module)**

```python
import csv

# Writing to CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "Delhi"])
    writer.writerow(["Bob", 30, "Mumbai"])

# Reading from CSV
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

---

# 🔹 **7. File Methods**

* `read(size)` → Reads `size` characters (or whole file if no size given).
* `readline()` → Reads a single line.
* `readlines()` → Reads all lines into a list.
* `write(text)` → Writes string to file.

---

# 🔹 **8. 10 Practice Problems with Code**

---

## **Q1. Write a program to create a text file and write 5 lines into it.**

```python
with open("myfile.txt", "w") as f:
    for i in range(1, 6):
        f.write(f"Line {i}\n")
```

---

## **Q2. Read the entire contents of the file.**

```python
with open("myfile.txt", "r") as f:
    print(f.read())
```

---

## **Q3. Read file line by line and print.**

```python
with open("myfile.txt", "r") as f:
    for line in f:
        print(line.strip())
```

---

## **Q4. Count number of words in a text file.**

```python
with open("myfile.txt", "r") as f:
    text = f.read()
    words = text.split()
    print("Word count:", len(words))
```

---

## **Q5. Append a new line into the file.**

```python
with open("myfile.txt", "a") as f:
    f.write("This is an appended line.\n")
```

---

## **Q6. Copy contents of one file to another.**

```python
with open("myfile.txt", "r") as f1, open("copy.txt", "w") as f2:
    f2.write(f1.read())
```

---

## **Q7. Write student details into a CSV file.**

```python
import csv
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "Grade"])
    writer.writerow(["Ravi", 20, "A"])
    writer.writerow(["Sita", 21, "B"])
```

---

## **Q8. Read and display student details from CSV.**

```python
import csv
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

---

## **Q9. Count number of lines in a text file.**

```python
with open("myfile.txt", "r") as f:
    lines = f.readlines()
    print("Number of lines:", len(lines))
```

---

## **Q10. Search for a word in a file and print line numbers.**

```python
word = "Line"
with open("myfile.txt", "r") as f:
    for num, line in enumerate(f, start=1):
        if word in line:
            print(f"Found '{word}' in line {num}: {line.strip()}")
```

---

✅ **Quick Recap:**

* `open(filename, mode)` opens files.
* Modes: `"r"`, `"w"`, `"a"`, `"r+"`.
* `read()`, `readlines()`, `write()` for file operations.
* Use `csv` module for structured data storage.


"""