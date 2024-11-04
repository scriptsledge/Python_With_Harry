a = int(input("Enter your age:"))

# if-elif-else ladder to handle multiple conditions
if a >= 18:  # Runs if age is 18 or above
    print("You are above the age of consent")
    print("Good for you")
elif a < 0:  # Runs if age is a negative value
    print("You are entering an invalid negative age")
elif a == 0:  # Runs if age is exactly 0
    print("You are entering 0, which is not a valid age")
else:  # Runs if age is between 1 and 17
    print("You are below the age of consent")

print("End of program!")
