# Merging dictionaries using the '|' operator, introduced in Python 3.9.
dict1 = {'a': 1, 'b': 2} 
dict2 = {'b': 3, 'c': 4} 
merged = dict1 | dict2  # Combines dictionaries; values in dict2 override those in dict1 for duplicate keys.
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}
