# Multiline string containing placeholders for name and date
letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

# Replace the placeholders with actual values using chaining of replace() functions
print(letter.replace("<|Name|>", "Script").replace("<|Date|>", "24-10-2024"))

# Explanation:
# - The variable 'letter' is a multiline string (using triple quotes) with placeholders '<|Name|>' and '<|Date|>'
# - The replace() function is used to replace '<|Name|>' with 'Script'
# - Another replace() function is chained to replace '<|Date|>' with '24-10-2024'
# - Chaining replace() functions allows multiple replacements in a single line
