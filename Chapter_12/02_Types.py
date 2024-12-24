# Type hints specify expected variable and function types for better readability and tooling support
age: int = 25  # 'age' is expected to be an integer

def greeting(name: str) -> str:  # 'name' should be a string, function returns a string
    return f"Hello, {name}!"

# Function usage
print(greeting("Alice"))  # Output: Hello, Alice!
