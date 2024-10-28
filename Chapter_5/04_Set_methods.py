s = {1, 5, 32, 54, 5, 5, "Cow"}
print(s, type(s))

# add(value): adds an element to the set
s.add(566)
print(s)

# remove(value): removes specified element; raises KeyError if not found
s.remove(1)
print(s)

# pop(): removes and returns an arbitrary element
s.pop()
print(s)

# discard(value): removes specified element without error if not found
s.discard("Cow")
print(s)

# clear(): removes all elements from the set
s.clear()
print(s)

# Examples of additional set methods:

example_set = {10, 20, 30}

# len(): returns the number of elements in the set
print(len(example_set))

# copy(): returns a shallow copy of the set
copy_set = example_set.copy()
print(copy_set)

# difference(other_set): returns elements in example_set but not in other_set
other_set = {20, 30, 40}
print(example_set.difference(other_set))  # Output: {10}
