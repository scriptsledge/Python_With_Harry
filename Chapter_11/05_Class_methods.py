# The '@classmethod' decorator in Python is used to define a class method.
# A class method is a method that is bound to the class rather than the instance of the class.

class Employee:
    # Class variable 'a'
    a = 0
    
    # Class method 'show'
    @classmethod
    def show(cls):
        # 'cls' is a reference to the class itself
        print(f"The value of a is {cls.a}")

# Creating an instance of the Employee class
e = Employee()

# Modifying the instance variable 'a' (does not affect the class variable 'a')
e.a = 45

# Calling the class method 'show' (uses the class variable 'a', not the instance variable)
e.show()