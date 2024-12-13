class Calculator:
    def __init__(self, num):
        self.num = num
    
    def square(self):
        print(f"Square of {self.num} is {self.num ** 2}")
    
    def cube(self):
        print(f"Cube of {self.num} is {self.num ** 3}")
    
    def sqroot(self):
        print(f"Square-root of {self.num} is {self.num ** 0.5}")

# Create an instance of Calculator with user input
num = Calculator(int(input("Enter the number: ")))
num.square()
num.cube()
num.sqroot()
