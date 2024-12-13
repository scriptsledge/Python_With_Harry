class Programmer:
    company = "Microsoft"  # Class attribute shared by all instances

    def __init__(self, name, salary, pin):
        # Constructor: Initializes instance-specific attributes
        self.name = name
        self.salary = salary
        self.pin = pin

# Creating two instances with individual attributes
dev1 = Programmer("Jaswat", "3000000", 234234)
dev2 = Programmer("Soooon", "2500000", 234235)

# Accessing both instance and class attributes
print(dev1.name, dev1.pin, dev1.salary, dev1.company)
print(dev2.name, dev2.pin, dev2.salary, dev2.company)
