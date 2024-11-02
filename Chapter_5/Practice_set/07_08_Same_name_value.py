# If keys (names) repeat, only the last value is kept; duplicate values are allowed
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

# Final dictionary output of friend-language pairs
print(favLan)

# Explanation:
# - `update({key: value})`: adds a key-value pair to the dictionary.
# - Duplicate keys overwrite with the latest value, while duplicate values are stored as they are.
