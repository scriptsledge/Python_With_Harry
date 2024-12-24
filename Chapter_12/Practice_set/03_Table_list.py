try:
    number = int(input("Enter the number: "))
    table = [number*i for i in range(1,11)]
    print(table)
except Exception as galti:
    print(f"Kuch to gadbad hai daya!\n{galti}")