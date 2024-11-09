# Function to remove a given word from a list and strip it at the same time
def rem(l, word):
    n = []  # Create an empty list to store modified items
    for item in l:  # Loop through each item in the input list
        if not(item == word):  # Check if the item is not equal to the given word
            # Strip removes leading and trailing occurrences of the specified word from the string
            n.append(item.strip(word))  # Strip the word from the item and add it to the new list
    return n  # Return the modified list

# Example list
l = ["annay", "Aniy", "San Andreas", "Jogmangal"]
print(rem(l, "an"))  # Call the function and print the result
