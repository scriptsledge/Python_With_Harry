class Employee:
    language = "Py"  # Class attribute shared by all objects
    salary = 2000000  # Another class attribute

# Create objects with unique attributes
sumit = Employee()
sumit.name = "Sumit Chouhan"  # Object-specific attribute
sushan = Employee()
sushan.name = "Sushan Raju"  # Object-specific attribute

# Accessing attributes
print(sumit.name, sumit.salary, sumit.language)  # Accesses class and object attributes
print(sushan.name, sushan.language, sushan.salary)

# Note:
# - `name` is specific to each object.
# - `language` and `salary` are shared across all instances unless explicitly overridden.
