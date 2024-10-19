from torch import slice_scatter


a = 'a' # this is a string
a = "apple" # this is also a string
a = '''bada
apple''' # this is also a string
# strings are immutable

# slicing
name = 'script'
print(len(name)) # we can know length of string using len function
sliced_string = name[2: 6] # start from index 2 all the way till 6 (excluding 6)
print(sliced_string)
print(name[1]) # to fetch a character

# indices starts from 0 (left to right)
# indices starts from -1 (right to left)