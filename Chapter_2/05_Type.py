# Using the type() function
a = 1
t = type(a)
print(t)  # Output: <class 'int'>

c = 22.55
t = type(c)
print(t)  # Output: <class 'float'>

a = "88.512"
t = type(a)
print(t)  # Output: <class 'str'>

# The type() function helps us know the type of any variable

# Type casting
b = float(a)  # Casts 'a' to a float
print(type(b))  # Output: <class 'float'>

# Similarly, we can cast variables to other types
b = int(float(a))  # Convert 'a' to float first, then to int
print(type(b))  # Output: <class 'int'>

b = str(c)  # Casts 'c' to a string
print(type(b))  # Output: <class 'str'>
