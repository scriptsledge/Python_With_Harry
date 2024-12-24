# try-else: The 'else' block executes if no exception occurs in the 'try' block
try:
    a = int(input("Hey, Enter a number: "))  # Try block to handle code that might raise an exception
    print(a)
except ValueError as e:  # Catches ValueError if input is not a number
    print(e)

else:
    print("I am inside else!")  # Executes if no exception occurred
