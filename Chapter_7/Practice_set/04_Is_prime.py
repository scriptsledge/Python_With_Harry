number = int(input("Enter the number:"))
for i in range(2, number):
    if number % i == 0:  # Check if number is divisible by i
        print(number, "is not a prime number!")
        break
else:
    print(number, "is a prime number!")
