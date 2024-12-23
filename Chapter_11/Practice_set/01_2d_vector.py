# Represents a 2D vector
class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

# Represents a 3D vector
class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

# Create instances of 2D and 3D vectors and print them
a = TwoDVector(1, 2)
a.show()
b = ThreeDVector(4, 4, 5)
b.show()