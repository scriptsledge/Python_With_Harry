# Function to print multiplication table of a given number
def print_table(digit):
    for i in range(1, 11):  # Loop from 1 to 10
        print(f"{digit} X {i} = {digit*i}")  # Print multiplication result

number = int(input("Enter the number: "))  # Take input from the user
print_table(number)  # Call the function with the input number
