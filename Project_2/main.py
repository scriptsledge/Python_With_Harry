import random

# Number guessing game with high score tracking
n = random.randint(1, 100)  # Generate random number between 1 and 100
a = -1  # Initialize user's guess
attempts = 0  # Track the number of attempts

# Loop until the correct number is guessed
while a != n:
    a = int(input("Guess the number: "))  # User input for guess
    if a < n:
        attempts += 1
        print("Too less! Think bigger!!")
    elif a > n:
        attempts += 1
        print("Too big! Climb down!!")

print("You guessed correct!")
print(f"You took {attempts} attempts!")

# Check and update high score
with open("C:\\Bits\\Python_With_Harry\\Project_2\\score.txt", 'r') as f:
    highScore = int(f.read())  # Read current high score from file

if attempts < highScore:  # Check if current attempts are fewer
    highScore = attempts
    with open("C:\\Bits\\Python_With_Harry\\Project_2\\score.txt", 'w') as f:
        f.write(f"{highScore}")  # Update high score in file

print(f"Highest score is {highScore}")
