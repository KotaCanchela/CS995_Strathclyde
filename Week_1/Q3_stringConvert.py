# Write a function that converts a string to an integer, by casting the string to an
# integer. If the string is not an integer, then the function should return None. The
# function should have one input argument and one return value. The input argument
# should be the string that is to be converted to an integer. The input argument should
# have the form "1242" or some other numeric value.
# The function should use try and except to catch the ValueError exception that is
# thrown if the string is not an integer. For example, if the function is provided with
# "1242sd" it should return None.

def string_convert(string):
    try:
        num = int(string)
        return num
    except ValueError:
        return None


test = "1234"

print(string_convert(test))