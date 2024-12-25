# filter a list of numbers which are divisible by 5
nums = [i for i in range(0,100)]
def divisible5(n):
    if n%5 == 0:
        return True

print(list(filter(divisible5, nums)))