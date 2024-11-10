'''
1 for snakee
-1 for water
0 for gun
'''
computer = -1
youStr = input("Enter your choice: ").lower()
youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"Snake", -1:"Water", 0:"Gun"}
you = youDict[youStr]

print(f"Computer chose {reverseDict[computer]}\nYou chose {reverseDict[you]}")
if (computer == you):
    print("It's a draw!")
else:
    if (computer == -1 and you == 1):
        print("You won!")
    elif (computer == -1 and you == 0):
        print("You lose!")
    elif (computer == 0 and you == -1):
        print("You won!")
    elif (computer == 0 and you == 1):
        print("You lose!")
    elif (computer == 1 and you == 0):
        print("You won!")
    elif (computer == 1 and you == -1):
        print("You lose!")
    else :
        print("Something went wrong!")