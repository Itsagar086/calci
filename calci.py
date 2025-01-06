import math
import cmath

# Function to perform basic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Error! Cannot compute the square root of a negative number."
    return math.sqrt(x)

def complex_add(x, y):
    return x + y

def complex_subtract(x, y):
    return x - y

def complex_multiply(x, y):
    return x * y

def complex_divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Trigonometric Functions
def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def logarithm(x, base=10):
    if x <= 0:
        return "Error! Logarithm of non-positive number."
    return math.log(x, base)

def factorial(x):
    if x < 0:
        return "Error! Factorial of negative number is undefined."
    return math.factorial(int(x))

# Complex number input handling
def complex_input(prompt):
    try:
        complex_number = complex(input(prompt))
        return complex_number
    except ValueError:
        print("Invalid complex number format. Please enter in a+bi format.")
        return complex_input(prompt)

# Main function to interact with the user
def calculator():
    print("Welcome to the Python Calculator!")
    while True:
        print("\nPlease select an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exponentiation (^)")
        print("6. Square Root (sqrt)")
        print("7. Trigonometric Functions (sin, cos, tan)")
        print("8. Logarithm (log)")
        print("9. Factorial (!)")
        print("10. Complex Number Operations")
        print("11. Exit")
        
        choice = input("Enter choice (1-11): ")

        # Handling basic operations
        if choice in ('1', '2', '3', '4', '5'):
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {add(x, y)}")
            elif choice == '2':
                print(f"Result: {subtract(x, y)}")
            elif choice == '3':
                print(f"Result: {multiply(x, y)}")
            elif choice == '4':
                print(f"Result: {divide(x, y)}")
            elif choice == '5':
                print(f"Result: {power(x, y)}")
        
        # Handling square root
        elif choice == '6':
            x = float(input("Enter number to find square root: "))
            print(f"Result: {sqrt(x)}")
        
        # Trigonometric Functions
        elif choice == '7':
            angle = float(input("Enter angle in degrees: "))
            print(f"sin({angle}) = {sine(angle)}")
            print(f"cos({angle}) = {cosine(angle)}")
            print(f"tan({angle}) = {tangent(angle)}")
        
        # Logarithm
        elif choice == '8':
            x = float(input("Enter number to compute logarithm: "))
            base = float(input("Enter base (default 10): ") or 10)
            print(f"Result: {logarithm(x, base)}")
        
        # Factorial
        elif choice == '9':
            x = float(input("Enter number to compute factorial: "))
            print(f"Result: {factorial(x)}")
        
        # Complex Number Operations
        elif choice == '10':
            print("Complex Number Operations:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            complex_choice = input("Enter choice (1-4): ")
            z1 = complex_input("Enter first complex number (a+bj): ")
            z2 = complex_input("Enter second complex number (a+bj): ")

            if complex_choice == '1':
                print(f"Result: {complex_add(z1, z2)}")
            elif complex_choice == '2':
                print(f"Result: {complex_subtract(z1, z2)}")
            elif complex_choice == '3':
                print(f"Result: {complex_multiply(z1, z2)}")
            elif complex_choice == '4':
                print(f"Result: {complex_divide(z1, z2)}")
        
        # Exit
        elif choice == '11':
            print("Thank you for using the calculator!")
            break
        
        else:
            print("Invalid input! Please try again.")

# Run the calculator
calculator()
