n = int(input("Enter the value of n:"))
dublicate = n  # Save the original value of n for later use
sum = 0  # Initialize sum to 0

# Loop to add all numbers from n down to 1
while (n > 0):
    sum += n  # Add current n to sum
    n -= 1  # Decrease n by 1 in each iteration

print("The sum of first", dublicate, "natural numbers is", sum)
