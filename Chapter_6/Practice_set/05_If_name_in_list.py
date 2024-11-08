name_list = ["Oswat", "Paon", "Aiti", "Neon"]
name = input("Enter your name:")

if name in name_list:  # Checks if the entered name exists within the list
    print("Your name is in the list.")
else:
    print("Your name is not in the list.")
