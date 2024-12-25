name = input("Enter your name: ")
marks = float(input("Enter your marks: "))
phoNo = int(input("Enter your phone number: "))

formated = (
    "The name of the student is {1}, his marks are {0} and phone number is {2}".format(
        marks, name, phoNo
    )
)

print(formated)
