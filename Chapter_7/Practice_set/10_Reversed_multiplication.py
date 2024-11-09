# Program to print the multiplication table of a number in reverse order

num = int(input("Enter the number: "))
for i in range(10, 0, -1):  # Loop from 10 down to 1
    print(f"{num} X {i} = {num * i}")
