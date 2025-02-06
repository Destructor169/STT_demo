# simple_calculator.py
"""
This module contains basic arithmetic operations including addition, subtraction,
multiplication, and division. It also provides a simple example of usage through
a main function.
"""

def add(a, b):
    """Adds two numbers."""
    return a + b

def subtract(a, b):
    """Subtracts the second number from the first."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers."""
    return a * b

def divide(a, b):
    """Divides the first number by the second, raises error on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    """
    Main function to demonstrate the calculator operations.
    It performs addition, subtraction, multiplication, and division on two numbers.
    """
    num1 = 10
    num2 = 5
    print(f"Sum: {add(num1, num2)}")
    print(f"Difference: {subtract(num1, num2)}")
    print(f"Product: {multiply(num1, num2)}")
    print(f"Division: {divide(num1, num2)}")

if __name__ == "__main__":
    main()
