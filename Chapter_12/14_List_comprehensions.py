# List Comprehensions: A concise way to create lists based on existing iterables.

myList = [1, 2, 3, 4, 5, 6]
squaredList = []

# Traditional approach using a for loop
for item in myList:
    squaredList.append(item * item)  # Appending square of each element
print(squaredList)

# Achieving the same result with list comprehension
print('*' * 20)
newList = [i * i for i in myList]  # Compact syntax to create a list of squares
print(newList)
