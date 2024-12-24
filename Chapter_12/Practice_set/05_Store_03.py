try:
    number = int(input("Enter the number: "))
    table = [number*i for i in range(1,11)]
    with open("C:\\Bits\\Python_With_Harry\\Chapter_12\\Practice_set\\Tables.txt", 'a')as f:
        f.write(f"Table of {number}: {str(table)}\n")
    
except Exception as galti:
    print(f"Kuch to gadbad hai daya!\n{galti}")