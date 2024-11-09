# Function to print a decreasing pattern of stars
def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

n = int(input("Enter the value of n: "))
pattern(n)
