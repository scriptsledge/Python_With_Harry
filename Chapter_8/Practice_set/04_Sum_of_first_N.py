# To calculate the sum of first n natural numbers using recursion
def calculate(n):
    if n == 1:  # Base case: sum of first 1 natural number is 1
        return 1
    return n + calculate(n - 1)  # Recursive step: add n to sum of first n-1 numbers

first_n = int(input("Enter the value of n: "))
print(f"The sum of first {first_n} natural number is {calculate(first_n)}")
