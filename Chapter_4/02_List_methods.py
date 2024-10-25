friends = ["Apple", 100, 738.33, True, 'z']
print(friends)

# append(): adds an element to the end of the list
friends.append(False)
print(friends)

l1 = [23, 45, 32, 0, 10, 100, 23, 1]

# sort(): sorts elements in ascending order
l1.sort()
print(l1)

# reverse(): reverses the order of elements
l1.reverse()
print(l1)

# insert(index, value): inserts a value at the specified index
l1.insert(1, 50)  # Insert 50 at index 1
print(l1)

# pop(index): removes and returns the element at the given index
print(l1.pop(4))  # Pops element at index 4
print(l1)

# remove(value): removes the first occurrence of the specified value
l1.remove(1)
print(l1)

# Additional examples of commonly used list methods:

# count(value): counts occurrences of the specified value
print(l1.count(23))  # Count of 23 in list

# index(value): returns the index of the first occurrence of the specified value
print(l1.index(100))  # Index of 100 in list

# extend(): extends list by appending elements from another list
extra_items = [200, 300]
l1.extend(extra_items)
print(l1)

# clear(): removes all elements from the list
l1.clear()
print(l1)
