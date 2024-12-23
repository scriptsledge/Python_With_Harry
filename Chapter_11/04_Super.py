# The 'super' function in Python is used to give access to methods and properties of a parent or sibling class.

# Base class: Employee
class Employee:
    def __init__(self):
        print("Constructor of Employee!")
    a = 1

# Intermediate class: Programmer, inherits from Employee
class Programmer(Employee):
    def __init__(self):
        # Calls the constructor of the parent class (Employee)
        super().__init__()
        print("Constructor of Programmer!")
    b = 2

# Derived class: Manager, inherits from Programmer
class Manager(Programmer):
    def __init__(self):
        # Calls the constructor of the parent class (Programmer), 
        # which in turn calls the constructor of Employee
        super().__init__()
        print("Constructor of Manager!")
    c = 3

o = Employee()
print(o.a)

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)