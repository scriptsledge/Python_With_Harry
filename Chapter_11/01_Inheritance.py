class Employee: # base/ parent class
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

# class Programmer(Employee):
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name of the Employee is {self.name} and the salary is {self.salary}")
#     def showLanguage(self):
#         print("The name is {self.name} and he is good with {self.language} language")

class Programmer(Employee): # inherited or child class
    company = "ITC Infotech"
    def showLanguage(self):
        print("The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()

print(a.company, b.company)