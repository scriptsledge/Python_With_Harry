# Tuple: similar to a list but immutable (cannot modify elements)
a = (1, 2, False, "Script", 1, 3.33, 'g')
b = ()         # Empty tuple
c = (1)        # Single element without comma, treated as int
d = (1,)       # Single element with comma, treated as tuple

print(type(a))  # Tuple
print(type(b))  # Tuple
print(type(c))  # Int
print(type(d))  # Tuple

# Uncommenting the line below will raise an error as tuples are immutable
# a[0] = 50 

# count(value): counts occurrences of the specified value in the tuple
no = a.count(1)
print(no)  # Count of 1 in tuple

# index(value): returns the index of the first occurrence of the specified value
i = a.index(1)
print(i)  # Index of 1 in tuple

# Additional tuple operations:

# len(): returns the length of the tuple
print(len(a))  # Length of tuple a

# max() and min() on tuples with numerical values only
num_tuple = (10, 20, 5, 30)
print(max(num_tuple))  # Maximum value
print(min(num_tuple))  # Minimum value

# concatenation: combining tuples (creates a new tuple)
t1 = (1, 2, 3)
t2 = (4, 5)
combined = t1 + t2
print(combined)

# repetition: repeats the tuple elements
repeated = t1 * 2
print(repeated)
