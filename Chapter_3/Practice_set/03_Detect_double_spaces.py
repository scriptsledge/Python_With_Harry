# String with spaces
name = "  this is  a string"

# No spaces
address = 'none'

# Find double spaces in 'name'
print(name.find("  "))  # Output: index of double spaces or -1 if not found

# Find double spaces in 'address'
print(address.find("  "))  # Output: -1 (not found)
