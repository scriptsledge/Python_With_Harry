import random

# Game options encoded as integers for simpler comparison
# 1 for Snake, -1 for Water, 0 for Gun
computer = random.choice([-1, 0, 1])  # Computer randomly selects Snake, Water, or Gun

# Mapping user input to game choices and vice versa
youStr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youDict.get(youStr, None)  # Convert user's choice to numeric representation

# Ensure valid input
if you is None:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    # Display choices
    print(f"Computer chose {reverseDict[computer]}\nYou chose {reverseDict[you]}")

    # Determine the outcome based on choices
    if computer == you:
        print("It's a draw!")
    else:
        if computer == -1 and you == 1:
            print("You won!")
        elif computer == -1 and you == 0:
            print("You lose!")
        elif computer == 0 and you == -1:
            print("You won!")
        elif computer == 0 and you == 1:
            print("You lose!")
        elif computer == 1 and you == 0:
            print("You won!")
        elif computer == 1 and you == -1:
            print("You lose!")
        else:
            print("Something went wrong!")
