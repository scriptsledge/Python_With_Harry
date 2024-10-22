# Escape sequences allow you to include special characters in strings that would otherwise be difficult to type.

# Example: Double quote within a string
example_1 = "She said, \"Hello!\""
print(example_1)  # Output: She said, "Hello!"

# Example: Newline character
example_2 = "Hello\nWorld"
print(example_2)  # Output:
# Hello
# World

# Example: Tab space
example_3 = "Hello\tWorld"
print(example_3)  # Output: Hello    World

# Example: Backslash
example_4 = "C:\\Users\\Username"
print(example_4)  # Output: C:\Users\Username

# Example: Single quote
example_5 = 'It\'s a beautiful day!'
print(example_5)  # Output: It's a beautiful day!

# Example: Backspace
example_6 = "Hello\b World"
print(example_6)  # Output: Hell World

# Example: Carriage return
example_7 = "Hello\rWorld"
print(example_7)  # Output: World

# Comprehensive example using multiple escape sequences
comprehensive_example = "HTML is a \"markup language\" for\n\tweb content,\nnot a programming language."
print(comprehensive_example)

# More examples
example_8 = 'Hello, World!\nWelcome to the Python tutorial.\tEnjoy learning!'
print(example_8)

example_9 = 'List of items:\n\t- Item 1\n\t- Item 2\n\t- Item 3'
print(example_9)