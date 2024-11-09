# Program to print a pyramid pattern using for loops

n = 3  # Number of rows for the pyramid
for i in range(1, n+1):
    # Print spaces to center-align the stars
    print(' ' * (n - i), end='')
    
    # Print '*' characters for the current row, forming a pyramid shape
    print('*' * ((2 * i) - 1))

#   *
#  ***
# *****