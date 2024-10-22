# Length of a string
str_1 = "Script"
str_2 = "sledge"
print(len(str_1))  # Outputs the length of str_1

# String methods
print(str_1.endswith("pt"))  # Checks if str_1 ends with "pt"
print(str_1.startswith("sc"))  # Checks if str_1 starts with "sc"
print(str_2.capitalize())  # Capitalizes the first letter of str_2

# More commonly used string functions:
print(str_1.upper())  # Converts all characters in str_1 to uppercase
print(str_2.lower())  # Converts all characters in str_2 to lowercase
print(str_1.replace("Script", "Code"))  # Replaces "Script" with "Code" in str_1
print(str_1.find("ri"))  # Finds the starting index of "ri" in str_1
print(str_2.isalpha())  # Checks if all characters in str_2 are alphabetic
print(str_1.isdigit())  # Checks if all characters in str_1 are digits
print("  hello  ".strip())  # Removes leading and trailing whitespace
print("a-b-c".split("-"))  # Splits the string by "-"