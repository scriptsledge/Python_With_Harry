# find the maximum of the numbers in a list using the reduce function
from functools import reduce


l = [23, 23, 35, 7, 324.78, 4363566, 653, 2, 1]

max = lambda a, b: a if a > b else b
print(reduce(max, l))
