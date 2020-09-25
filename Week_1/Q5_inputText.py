# An input text string contains newline characters and additional spaces, together with
# commas. Write a function that:
# • Removes the newline characters.
# • Splits the string using the comma character.
# • Removes any leading and trailing white space from the resulting substrings.
# • Returns the resulting list of values.
# Create a test text string to demonstrate that the function works as expected.
# The function should have one input argument and one return value. The input
# argument should be in the input string, whereas the return value should be the
# resulting list.


def reformat_text(string):
    string = string.replace("\n", "")
    splitString = string.split(",")
    reformatted_String = []
    for line in splitString:
        reformatted_String.append(line.strip())
    return reformatted_String


testString = "Hello, how are you? I\n am great, thank you. \nHow are you?   "

if __name__ == "__main__":
    print(reformat_text(testString))
