# Inheritance allows a child class to acquire properties and methods from a parent class.

class Employee:  # Parent class
    company = "ITC"  # Class attribute for the Employee class

    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

class Programmer(Employee):  # Child class inheriting from Employee
    company = "ITC Infotech"  # Overriding the 'company' attribute

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

# Instances of the parent and child classes
a = Employee()
b = Programmer()

# Accessing class attributes
print(a.company)  # Outputs 'ITC' from the Employee class
print(b.company)  # Outputs 'ITC Infotech' from the Programmer class
