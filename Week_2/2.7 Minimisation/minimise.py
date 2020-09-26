import testFunction
from testFunction import testFunction
import random

x = 1.5
y = testFunction(x)

print(f"testFunction({str(x)}) = {str(y)}")

# EXERCISE 2

listNum = []
for i in [float(j) / 100 for j in range(-199, 500)]:
    # Adds all numbers that are -2 < x < 5 to the list called listNum
    listNum.append(i)


testFunctionValues = []
for num in listNum:
    testFunctionValues.append(testFunction(num))

# Print minimum and maximum of values from -2 < x < 5 that are increments of 0.01
# that use the testFunction function.

print(min(testFunctionValues))
print(max(testFunctionValues))

# EXERCISE 3

# Pick three random values from the list of nums and append them to a new list
threeRandVal = []
for i in range(3):
    threeRandVal.append(random.choice(listNum))

# Select the two lowest values of the three
threeRandVal.sort()
del threeRandVal[2]

# Select a new third value at random between the two remaining values
