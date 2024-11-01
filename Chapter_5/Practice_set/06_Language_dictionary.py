favLan = {}  # Dictionary to store friends' favorite languages

# Adding friend's name and language preference
myKey = input("Enter friend's name:")
myValue = input("Enter language name:")
favLan.update({myKey: myValue})

myKey = input("Enter friend's name:")
myValue = input("Enter language name:")
favLan.update({myKey: myValue})

myKey = input("Enter friend's name:")
myValue = input("Enter language name:")
favLan.update({myKey: myValue})

myKey = input("Enter friend's name:")
myValue = input("Enter language name:")
favLan.update({myKey: myValue})

myKey = input("Enter friend's name:")
myValue = input("Enter language name:")
favLan.update({myKey: myValue})

# Printing the final dictionary of friend-language pairs
print(favLan)

# Explanation:
# - `update({key: value})` adds a new key-value pair to the dictionary.
# - If the key already exists, the value is updated with the new input.
