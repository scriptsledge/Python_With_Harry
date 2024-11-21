import random

def game():
    print("You are playing the game...")
    score = random.randint(1, 62)  # Random score generation
    print(f"Your score: {score}")

    # Read the current high score from the file
    with open("Chapter_9/Practice_set/hiScore.txt") as f:
        hiScore = f.read()
        hiScore = int(hiScore) if hiScore != "" else 0  # Handle empty file case

    # Update the high score if the current score is higher
    if score > hiScore:
        with open("Chapter_9/Practice_set/hiScore.txt", "w") as f:
            f.write(str(score))
            print("New high score achieved!")

    return score

game()
