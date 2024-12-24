# __name__
def myFunc():
    print("Running from module.py")

# __name__ will be "__main__" if this file is run directly
# If this file is imported as a module, __name__ will be the module's name
print(__name__)

# This block only executes if the file is run directly
# It won't run if the file is imported as a module
if __name__ == "__main__":
    myFunc()
    print("Not meant to run in '11__main__.py'")