# Dictionary: stores key-value pairs, allowing efficient value retrieval by unique keys
marks = {
    "Asmit": 70,
    "Prasoon": 70,
    "Dhruv": 50,
    "Tausif": 80
}

# Dictionary lookup: O(1) time complexity for key-based access
print(marks, type(marks))

# Accessing a value by key
print(marks["Prasoon"])

# Properties of dictionaries:
# - Unordered: no guaranteed order for elements
# - Mutable: values can be changed
# - Indexed by unique keys (duplicates not allowed)
