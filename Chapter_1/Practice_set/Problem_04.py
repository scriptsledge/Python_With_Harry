# write code to print contents of a directory using os module
import os

def list_directory_contents(path='.'):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"The directory {path} does not exist.")
    except PermissionError:
        print(f"Permission denied to access {path}.")

# Example usage
list_directory_contents('/')