# multiplication using while loop
digit = int(input("Enter the number:"))
number = digit
while (number <= digit * 10):  # Printing 1 to 10 multiples of the entered number
    print(number)
    number += digit
