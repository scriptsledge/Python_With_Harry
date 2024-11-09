# using functions to find greatest of three numbers
def greatest_num(a, b, c):
    return max(a, b, c)  # Using built-in function 'max' to find the greatest number

x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))

great = greatest_num(x, y, z)  # Function call with three arguments
print(great)
