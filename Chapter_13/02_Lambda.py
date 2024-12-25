# Lambda Expressions: Create small, anonymous functions with a single expression.
# Useful for short, quick operations without formally defining a function.

# Traditional function to square a number
def square(n): 
    return n * n

# Lambda function for the same operation
sq = lambda x: x * x  # Takes input `x` and returns `x * x`

# Example usage
print(square(4))  # Output: 16 (using traditional function)
print(sq(4))      # Output: 16 (using lambda function)
