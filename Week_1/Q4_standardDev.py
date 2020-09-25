import statistics
import math

# Write a function to compute the sample standard deviation of floating point input
# values that are provided in a list. The function should have one input argument and
# one return value. The input argument should be a list of input values and the return
# argument should be the sample standard deviation.
# The function should return None when the input list contains zero or one element. If
# the input list contains two or more values, then it should return the sample standard
# deviation




def standard_deviation(listNums):
    if len(listNums) <= 1:
        return None
    return statistics.stdev(listNums)


def variance(data, ddof=0):
     n = len(data)
     mean = sum(data) / n
     return sum((x - mean) ** 2 for x in data) / (n - ddof)


def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev

listIntegers = [2, 2.53, 6, 7.36]

print(standard_deviation(listIntegers))
