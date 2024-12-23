class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, c2):
        """Add two complex numbers."""
        return Complex(self.real + c2.real, self.imag + c2.imag)
    
    def __mul__(self, c2):
        """Multiply two complex numbers."""
        real_part = self.real * c2.real - self.imag * c2.imag
        imag_part = self.real * c2.imag + self.imag * c2.real
        return Complex(real_part, imag_part)

    def __str__(self):
        """Return a string representation of the complex number."""
        return f"{self.real} + {self.imag}i"

# Example usage:
c1 = Complex(1, 2)
c2 = Complex(3, 4)
print("c1 =", c1)
print("c2 =", c2)
print("c1 + c2 =", c1 + c2)
print("c1 * c2 =", c1 * c2)