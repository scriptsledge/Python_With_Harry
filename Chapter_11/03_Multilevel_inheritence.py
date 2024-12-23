# Demonstrating multilevel inheritance and the use of the 'super' function

# Base class: Employee
class Employee:
    # Constructor method that gets called when an object is created
    def __init__(self):
        print("Constructor of Employee!")
    
    # Class variable 'a' shared among all instances of Employee
    a = 1


# Intermediate class: Programmer, inherits from Employee
class Programmer(Employee):
    # Constructor method that gets called when an object is created
    def __init__(self):
        # Using 'super' to call the constructor of the parent class (Employee)
        super().__init__()
        print("Constructor of Programmer!")
    
    # Class variable 'b' shared among all instances of Programmer
    b = 2


# Derived class: Manager, inherits from Programmer (and indirectly from Employee)
class Manager(Programmer):
    # Constructor method that gets called when an object is created
    def __init__(self):
        # Using 'super' to call the constructor of the parent class (Programmer)
        super().__init__()
        print("Constructor of Manager!")
    
    # Class variable 'c' shared among all instances of Manager
    c = 3


# Creating objects and accessing class variables
o = Employee()
print(o.a)  # Accessing class variable 'a' of Employee

o = Programmer()
print(o.a, o.b)  # Accessing class variables 'a' (inherited) and 'b' of Programmer

o = Manager()
print(o.a, o.b, o.c)  # Accessing class variables 'a' (inherited), 'b' (inherited), and 'c' of Manager