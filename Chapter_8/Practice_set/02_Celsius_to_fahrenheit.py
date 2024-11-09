# function to convert Celsius to Fahrenheit
def celToFeh(val):
    return (val * 9/5) + 32  # Conversion formula from Celsius to Fahrenheit

celVal = int(input('Enter the value in Celsius: '))  # Taking Celsius input from user
print(f"{celVal} °Celsius = {celToFeh(celVal)} °Fahrenheit")  # Printing the converted value
