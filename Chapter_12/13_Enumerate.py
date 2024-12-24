# enumerate: A built-in Python function that adds a counter to an iterable and returns an enumerate object

# Traditional way - manually tracking index
l = [2, 34, 23, 564, 657]

index = 0
for number in l:
    print(f"Number at index {index} is {number}")
    index += 1  # Manually incrementing index - prone to errors and less readable

print('*'*20)

# Modern way using enumerate
# enumerate(iterable, start=0) returns tuple pairs of (index, value)
for index, number in enumerate(l):
    # Automatically handles index tracking and value unpacking
    print(f"Number at index {index} is {number}")