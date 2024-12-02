class Employee:
    language = "Py"
    salary = 2000000

    def getInfo(self):
        # Accesses attributes of the instance (or class if not overridden by the instance)
        print(f"The language is {self.language} and salary is {self.salary}")

    @staticmethod
    def greet():
        # Static method: Doesn't depend on instance-specific data
        print("Good morning!!")

sumit = Employee()
sumit.language = "JavaScript"

sumit.getInfo()  # Calls the instance method, using `sumit`'s attributes
Employee.getInfo(sumit)  # Equivalent, explicitly passing the instance

sumit.greet()  # Calls the static method, not tied to any instance
