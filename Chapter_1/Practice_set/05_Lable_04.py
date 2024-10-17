# Lable Problem_04 with comments

# importing os module
import os

# defining function
def list_directory_contents(path='.'):
    # handling error
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"The directory {path} does not exist.")
    except PermissionError:
        print(f"Permission denied to access {path}.")

# give directory path inside single quotes
list_directory_contents('/')