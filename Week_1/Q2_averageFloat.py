# Write a function that returns the average value of input floating point values that
# are provided in a list. The function should have one input argument and one return
# value. The input argument should be the list and return value should be the average.
# If the input list is empty, then the function should return None.


def average_float(nums):
    average = 0
    if len(nums) == 0:
        return None
    numCount = 0
    for num in nums:
        numCount += 1
        average += num
    if average > 0:
        averageNum = average / numCount
    return averageNum


listFloats = [5.02, 5.75, 8.42]

print(average_float(listFloats))
