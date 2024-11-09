# Function to convert inches to centimeters
def inchToCm(val):
    return val * 2.54  # Conversion factor: 1 inch = 2.54 cm

inchVal = float(input("Enter the value in inch: "))
print(f"{inchVal} inch = {inchToCm(inchVal)} cm")
