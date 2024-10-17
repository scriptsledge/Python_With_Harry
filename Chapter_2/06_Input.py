# Using the input() function
a = input("Enter number 1: ")  # Input from user, stored as a string
b = input("Enter number 2: ")  # Input from user, stored as a string

print("Number a is:", a)  # Output the value of 'a'
print("Number b is:", b)  # Output the value of 'b'

# Why "12"? Because by default, input() takes data as a string
print("Sum as strings is:", a + b)  # Concatenates the strings 'a' and 'b'

# To perform arithmetic, convert the input strings to integers
print("Sum as integers is:", int(a) + int(b))  # Adds 'a' and 'b' as integers
