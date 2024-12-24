a = 4
b = 0
try:
    b = int(input("Enter the value of b: "))
    print(f"a/b = {a/b}")
except ZeroDivisionError:
    print("Infinity!!")