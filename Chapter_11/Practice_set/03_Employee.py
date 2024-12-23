class Employee:
    """
    Represents an employee with a salary and increment.
    """

    # Base salary and increment percentage
    salary = 100000
    increment = 100

    @property
    def salaryAfterIncrement(self):
        """
        Calculates salary after increment.
        """
        return self.salary + (self.salary * self.increment / 100)
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        """
        Updates increment percentage based on new salary.
        """
        self.increment = ((salary / self.salary) - 1) * 100

# Example usage:
e = Employee()
e.salary = 200
e.increment = 20
print(e.salaryAfterIncrement)

e.salaryAfterIncrement = 500
print(e.increment)