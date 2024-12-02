class Employee:
    language = "Py"  # Class attribute
    salary = 2000000  # Class attribute

sumit = Employee()
sumit.language = "JavaScript"  # Instance attribute overrides the class attribute

# Accessing attributes
print(sumit.salary, sumit.language)
