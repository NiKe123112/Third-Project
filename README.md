# Python Error Handling – Try and Except

This is a beginner-friendly Python project that demonstrates how to handle errors gracefully using `try`, `except`, and `finally` blocks.

## 📌 What This Project Does

- Takes input from the user.
- Handles invalid input using `try` and `except`.
- Shows how to avoid crashes and provide user-friendly error messages.

## 💡 Features

- Input validation
- Exception handling
- Clean and simple code for understanding error management in Python

## 🛠️ Example Code

```python
try:
    num = int(input("Enter a number: "))
    print("Your number is:", num)
except ValueError:
    print("That was not a valid number.")
finally:
    print("Program finished.")
