# break and continue - control flow statements in loops

# break: Exits the loop immediately when a condition is met
for i in range(10):  
    if (i == 3):  
        break  # Exits the loop when i equals 3
    print(i)  # Prints i values until i == 3

print("======================")

# continue: Skips the current iteration and proceeds to the next one
for i in range(10):
    if (i == 3):
        continue  # Skips printing i when i equals 3
    print(i)  # Prints all i values except when i == 3
