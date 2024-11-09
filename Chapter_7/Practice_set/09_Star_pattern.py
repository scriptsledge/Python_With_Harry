# Program to print a square pattern with filled borders and empty center

n = 3  # Size of the square
for i in range(n):
    if i == 0 or i == n - 1:  # First and last row: fully filled with '*'
        print('*' * n)
    else:  # Middle rows: '*' on the borders, spaces in the middle
        print('*', end='')      # Left border '*'
        print(' ' * (n - 2), end='')  # Middle spaces
        print('*')               # Right border '*'

# ***
# * *
# ***