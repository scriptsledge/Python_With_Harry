# map: Applies a function to all items in an iterable.
l = [1, 2, 3, 4, 5, 6]
square = lambda x: x * x
sqList = map(square, l)  # Maps the square function to each element of the list
print(list(sqList))  # Output: [1, 4, 9, 16, 25, 36]

# filter: Filters items in an iterable based on a function's condition.
def even(n):
    return n % 2 == 0  # Returns True for even numbers

onlyEven = filter(even, l)  # Filters only even numbers
print(list(onlyEven))  # Output: [2, 4, 6]

# reduce: Reduces an iterable to a single value using a function.
from functools import reduce
sum = lambda a, b: a + b
print(reduce(sum, l))  # Sums up all elements in the list. Output: 21

def mul(a, b):
    return a * b

print(reduce(mul, l))  # Multiplies all elements in the list. Output: 720
