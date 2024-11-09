# recursion
def factorial(n):
    if(n==1 or n==0):  # Base case: if n is 0 or 1, return 1
        return 1
    return n * factorial(n-1)  # Recursive call with n-1

n = int(input("Enter a number: "))
print(f"Factorial of {n} is {factorial(n)}")
