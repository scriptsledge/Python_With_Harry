# Multiple inheritance allows a class to inherit attributes and methods from multiple parent classes.

class Employee:  # First parent class
    company = "ITC"
    name = "Default name"

    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:  # Second parent class
    language = "Python"

    def printLanguage(self):
        print(f"Out of all the languages, your language is: {self.language}")

class Programmer(Employee, Coder):  # Child class inheriting from Employee and Coder
    company = "ITC Infotech"  # Overriding 'company' attribute from Employee

    def showLanguage(self):
        print(f"The company is {self.company}, and the programmer is proficient in {self.language} language")

# Creating instances
a = Employee()  # Instance of Employee
b = Programmer()  # Instance of Programmer, inheriting from both Employee and Coder

# Accessing attributes and methods
print(a.company, b.company)  # Shows how class attributes differ between parent and child classes
b.show()  # Method from Employee class
b.printLanguage()  # Method from Coder class
b.showLanguage()  # Method specific to Programmer class
