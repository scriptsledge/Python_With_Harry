# Original string with double spaces
name = "  this is  a string"

# 'replace' returns a new string by substituting "  " with " " (double space with single)
print(name.replace("  ", " "))

# Original string remains unchanged due to string immutability
print(name)
