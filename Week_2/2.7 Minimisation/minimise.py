import testFunction
from testFunction import testFunction

x = 1.5
y = testFunction(x)

print(f"testFunction({str(x)}) = {str(y)}")


listNum = []
for i in [float(j) / 100 for j in range(-199, 500)]:
    # Adds all numbers that are -2 < x < 5 to the list called listNum
    listNum.append(i)


testFunctionValues = []
for num in listNum:
    testFunctionValues.append(testFunction(num))

