# Handling exceptions for robust code execution
try:
    a = int(input("Hey, Enter a number: "))  # Converts input to integer
    print(a)  # Prints the integer if input is valid
except ValueError as e:  # Handles specific error if input is not an integer
    print(e)  # Prints the error message

print("Thank You!!")  # Executes regardless of exception
