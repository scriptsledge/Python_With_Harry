a = int(input("Enter your age:"))

# Independent if statement to check even number
if a % 2 == 0:
    print("a is even")

# Separate if-elif-else to evaluate age
if a >= 18:
    print("You are above the age of consent")
elif a < 0:
    print("You are entering an invalid negative age")
elif a == 0:
    print("You are entering 0, which is not a valid age")
else:
    print("You are below the age of consent")

print("End of program!")
