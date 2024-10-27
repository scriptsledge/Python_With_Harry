# Set: collection of unique, unordered values
s = {1, 5, 32, 54, 5, 5}  # Duplicates are automatically removed
e = set()  # Empty set
t = {}     # Empty dictionary, not a set

print(type(e))  # Shows that e is a set
print(type(t))  # Shows that t is a dictionary

# Sets do not allow repeated values
print(s)  # Output will contain unique values only: {1, 5, 32, 54}
