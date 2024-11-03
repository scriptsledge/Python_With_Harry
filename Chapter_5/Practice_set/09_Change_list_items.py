# Sets cannot contain mutable elements, such as lists
s = {8, 7, 12, "Harry", [1, 2]}  # TypeError: lists are mutable and not allowed in sets

# Explanation:
# - Sets require elements to be immutable (unchangeable) for hashability.
# - Allowed types in sets include integers, floats, strings, and tuples (if they are fully immutable).
# - Lists are mutable, so attempting to add a list `[1, 2]` to a set will raise an error.
