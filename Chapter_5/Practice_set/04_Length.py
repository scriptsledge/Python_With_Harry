# Set to demonstrate how values are stored
s = set()

s.add(20)      # Adding integer 20
s.add(20.0)    # Adding float 20.0 (considered equal to integer 20 in sets)
s.add('20')    # Adding string '20' (unique, different from 20 or 20.0)

# Expected length of s is 2 because 20 and 20.0 are considered equal in value
print(s)       # Output: {20, '20'}
print(len(s))  # Output: 2

# Explanation:
# - In sets, `20` and `20.0` are considered the same due to value equality, 
#   so only one of them is stored.
# - The string '20' is unique and stored separately.
