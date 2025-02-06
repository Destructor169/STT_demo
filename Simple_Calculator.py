# simple_calculator.py

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
    num1 = 10
    num2 = 5
    print(f"Sum: {add(num1, num2)}")
    print(f"Difference: {subtract(num1, num2)}")
    print(f"Product: {multiply(num1, num2)}")
    print(f"Division: {divide(num1, num2)}")

if __name__ == "__main__":
    main()
