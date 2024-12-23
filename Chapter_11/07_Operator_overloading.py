# Operator Overloading in Python
# Operator overloading allows developers to redefine the behavior of operators when working with user-defined objects.

class Number:
    def __init__(self, n):
        # Initialize the Number object with a value 'n'
        self.n = n
    
    # Overload the '+' operator to add two Number objects
    def __add__(self, num):
        # Return the sum of the values of the two Number objects
        return self.n + num.n

# Create two Number objects
n = Number(1)
m = Number(2)

# Use the overloaded '+' operator to add the two Number objects
print(n + m)

# Other operator overloading methods:
# p1 + p2  # p1.__add__(p2)
# p1 - p2  # p1.__sub__(p2)
# p1 * p2  # p1.__mul__(p2)
# p1 / p2  # p1.__truediv__(p2)
# p1 // p2 # p1.__floordiv__(p2)

# Special methods for string representation and length:
# __str__() # used to set what gets displayed upon calling str(obj)
# __len__() # used to set what gets displayed upon calling len(obj)