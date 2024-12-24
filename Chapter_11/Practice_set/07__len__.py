class Vector:
    def __init__(self, lis):
        self.len = len(lis)  # Store the vector's dimension
        self.x = lis[0]      # X-component
        self.y = lis[1]      # Y-component
        self.z = lis[2]      # Z-component

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"  # String representation of the vector
    
    def __len__(self):
        return self.len  # Enable len() to return vector's dimension

v = Vector([7, 8, 10])
print(f"{v}\n{len(v)}")  # Output vector and its dimension using overloaded methods
