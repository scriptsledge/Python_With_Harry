# The '@property' decorator in Python is used to define a getter method for a property.
# It allows for more fine-grained control over attribute access and modification.

class Employee:
    # Property 'name' with getter method
    @property
    def name(self):
        # Returns the full name by concatenating first and last names
        return f"{self.fname} {self.lname}"
    
    # Setter method for property 'name'
    @name.setter
    def name(self, value):
        # Splits the input string into first and last names
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

# Creating an instance of the Employee class
e = Employee()

# Setting the 'name' property (calls the setter method)
e.name = "Khatti Cherry"

# Getting the 'name' property (calls the getter method)
print(e.name)