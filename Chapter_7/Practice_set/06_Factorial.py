# Program to calculate factorial using a for loop

n = int(input("Enter the value of n:"))
factorial = 1  # Initializing the factorial variable to 1

# Loop from 1 to n to multiply each integer with factorial
for i in range(1, n+1):
    factorial *= i  # Update factorial by multiplying with the current value of i

# Output the computed factorial value
print("The factorial of", n, "is", factorial)
