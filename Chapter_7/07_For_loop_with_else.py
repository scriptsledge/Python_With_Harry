# for loop with else - The else block is executed when the loop finishes all iterations without encountering a break statement
l = [1, 7, 8]
for item in l:  # Loops through each item in the list
    print(item)  # Prints each item
else:
    print("done")  # Executes after the loop completes, when no break occurs
