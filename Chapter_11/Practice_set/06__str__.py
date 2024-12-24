# Define a class Vector to represent 3D vectors
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Return a string representation of the vector
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"


# Create a Vector object
v = Vector(7, 8, 10)

# Print the vector
print(v)