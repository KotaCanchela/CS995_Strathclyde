# Write a function that converts one of {"one", "two", "three", "four", "five",
# "six", "seven", "eight", "nine", "ten"} into a corresponding integer value.
# For example, the function should return 1 when it is given "one".
# The function should have one input argument and one return value. The input
# argument should be a string and the return value should be an integer


def convert_num():

    dictNum = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
    }

    askNum = input("What number are you looking for?")

    print(dictNum[askNum])


convert_num()


dictText = {"hello": "hi"}

print(dictText["hello"])
