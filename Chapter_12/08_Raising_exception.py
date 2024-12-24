# Raising exceptions for custom error handling
a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if b == 0:  # Check for division by zero
    raise ZeroDivisionError("Hey, our program is not meant to divide numbers by zero")  # Raises custom exception
else:
    print(f"The division a/b is {a/b}")  # Performs division if no error
