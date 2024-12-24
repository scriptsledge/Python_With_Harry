# The walrus operator (:=) allows assignment within expressions
if (n := len([1, 2, 3, 4, 5])) > 3:  # Assign length to 'n' while checking the condition
    print(f"List is too long ({n} elements, expected <= 3)")
# Output: List is too long (5 elements, expected <= 3)
