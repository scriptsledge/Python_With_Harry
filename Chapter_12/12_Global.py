# Global: The `global` keyword allows modifying a variable defined outside a function.

a = 0  # Global variable

def fun():
    global a  # Access and modify the global variable
    a = 1  # Changing the value of the global variable
    print(a)  # Prints updated value of 'a' within the function

fun()
print(a)  # Prints updated value of 'a' in the global scope
