class Employee:
    language = "Python"
    salary = 1200000

    def __init__(self, name, salary, lang):
        # Constructor (dunder method): Automatically sets instance-specific attributes
        self.name = name
        self.salary = salary
        self.language = lang
        print("I'm creating an object!")

    def getInfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")

    @staticmethod
    def greet():
        # Static method: Doesn't rely on instance-specific data
        print("Good morning!!")

# Creating an instance with specific attributes
sumit = Employee("Sumit", 1300000, "Javascript")
print(sumit.name, sumit.salary, sumit.language)
