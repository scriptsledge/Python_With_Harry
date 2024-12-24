# try-finally: The 'finally' block runs no matter what, even if the function returns or an exception occurs
def main():
    try:
        a = int(input("Hey, Enter a number: "))  # Try block to execute potentially error-raising code
        print(a)
        return  # Function returns, but finally still executes
    
    except ValueError as e:  # Catches ValueError if input is not a valid number
        print(e)
        return  # Function returns here, but finally still executes

    finally:  # Ensures this block runs regardless of earlier returns or exceptions
        print("I am inside finally!")

main()
