# Calculate the square of a number entered by the user

# Take input for the number
number = int(input("Enter the number you want the square of: "))

# Calculate the square of the number
square = number ** 2  # Using the exponentiation operator
# square = number * number  # Alternative valid method
# square = number^2  # Incorrect: ^ is the bitwise XOR operator

# Print the result
print("Square of", number, "is", square)
