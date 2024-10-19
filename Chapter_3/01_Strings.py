# String examples
a = 'a'          # This is a string
a = "apple"      # This is also a string
a = '''badaapple'''  # This is also a string

# Strings are immutable

# Slicing example
name = 'script'

# Get the length of the string
print(len(name))  # Output: 6

# Slicing the string
sliced_string = name[2:6]  # Start from index 2 up to (but not including) index 6
print(sliced_string)       # Output: 'ript'

# Fetching a character by index
print(name[1])  # Output: 'c'

# Note:
# Indices start from 0 (left to right)
# Indices start from -1 (right to left)
