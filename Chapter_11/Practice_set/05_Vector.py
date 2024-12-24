# Define a class Vector to represent 3D vectors
class Vector:
    # Initialize a Vector object with x, y, and z coordinates
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Overload the addition operator to add two vectors
    def __add__(self, other):
        # Create a new Vector object with the sum of corresponding coordinates
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    # Overload the multiplication operator to calculate the dot product of two vectors
    def __mul__(self, other):
        # Calculate the dot product using the formula: x1*x2 + y1*y2 + z1*z2
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result

    # Overload the string representation of a Vector object
    def __str__(self):
        # Return a string in the format "Vector(x, y, z)"
        return f"Vector({self.x}, {self.y}, {self.z})"


# Create three Vector objects
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)


# Test vector addition and dot product
print(v1 + v2)  # Output: Vector(5, 7, 9)
print(v1 * v2)  # Output: 32

print(v1 + v3)  # Output: Vector(8, 10, 12)
print(v1 * v3)  # Output: 50