import random

# Randomly select an option for the computer: 1 for Snake, -1 for Water, 0 for Gun
computer = random.choice([-1, 0, 1])

# Mapping user input to game choices and numeric representations
youStr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youDict.get(youStr, None)

# Validate user input
if you is None:
    print("Invalid input!\nPlease enter 's', 'w', or 'g'.")
else:
    # Display choices made by both the computer and the user
    print(f"Computer chose {reverseDict[computer]}\nYou chose {reverseDict[you]}")

    # Check the result:
    # If `computer - you` equals -1 or 2, the user loses.
    # Otherwise, if not a draw, the user wins.
    if computer == you:
        print("It's a draw!")
    elif (computer - you == -1 or computer - you == 2):
        print("You lose!")
    else:
        print("You win!")
