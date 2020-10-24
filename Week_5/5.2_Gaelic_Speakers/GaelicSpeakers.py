import csv

"""
A function to read the Gaelic understanding categories.
"""
def readCategories(row, categoryForColumn):
    nColumns = len(row)
    for iColumn in range(nColumns):

        category = row[iColumn]
        if len(category) == 0:
            continue

        if category in categoryForColumn.values():
            print("Error: already have read the category \"" + category + "\"")
            continue

        categoryForColumn[iColumn] = category

"""
A function to load census data on Gaelic understanding.
"""
def loadData(fileName, areas):
    areas.clear()

    # Open input CSV file.
    inputFile = open(fileName, "r", encoding = "ISO-8859-1")
    csvReader = csv.reader(inputFile)

    categoryForColumn = {}

    for row in csvReader:

        # Skip the header information.
        if csvReader.line_num < 5:
            continue

        # Read the categories.
        if csvReader.line_num == 5:
            readCategories(row, categoryForColumn)
            continue

        # Read the data table.
        nColumns = len(row)
        area = ""
        sex = ""
        age = ""
        categories = {}
        for iColumn in range(nColumns):
            value = row[iColumn]
            if iColumn == 0:
                area = value
            elif iColumn == 1:
                sex = value
            elif iColumn == 2:
                age = value
            else:
                category = categoryForColumn[iColumn]
                if value == "-":
                    value = "0"
                categories[category] = value

        # Only need "All" people.
        if not sex.startswith("All "):
            continue

        # Add keys if they are not present.
        if area not in areas.keys():
            areas[area] = {}
        if age not in areas[area].keys():
            areas[area][age] = categories

    inputFile.close()

"""
A function to count the number of Gaelic speakers in an area.
"""
def countSpeakers(areas, speakingCategories, absoluteSpeakers, relativeSpeakers):
    absoluteSpeakers.clear()
    relativeSpeakers.clear()

    for area in areas.keys():

        # Only consider electoral wards.
        if area == "Scotland":
            continue

        # Count the total speakers within this area.
        totalSpeakers = 0
        totalPopulation = 0
        ages = areas[area]
        for age in ages.keys():
            if age != "Total":
                continue

            categories = ages[age]

            for category in categories.keys():
                # The numbers contain commas that must be removed first.
                intValue = int(categories[category].replace(",",""))

                # Record the total number of people.
                if category == "All people aged 3 and over":
                    totalPopulation = intValue
                    continue

                # Only sum the Gaelic speakers.
                if not category in speakingCategories:
                    continue
                totalSpeakers += intValue

        absoluteSpeakers[area] = totalSpeakers
        relativeSpeakers[area] = float(totalSpeakers)/totalPopulation

"""
A function to print the top three within a dictionary, 
ordering the data by the value in the dictionary.
"""
def printTopThree(dictionary):
    pairs = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    n = len(pairs)
    for i in range(n):
        print("Electral ward: " + pairs[i][0] + ", Value:" + str(pairs[i][1]))
        if i == 2:
            break

"""
A program to find the electoral wards in Scotland with the highest
number of Gaelic speakers.
"""
if __name__ == "__main__":
    areas = {}
    loadData("DC2120SC.csv", areas)

    speakingCategories = []
    speakingCategories += ["Speaks, reads and writes Gaelic"]
    speakingCategories += ["Speaks but does not read or write Gaelic"]
    speakingCategories += ["Speaks and reads but does not write Gaelic"]

    absoluteSpeakers = {} # absolute speakers per area
    relativeSpeakers = {} # relative speakers per area
    countSpeakers(areas, speakingCategories, absoluteSpeakers, relativeSpeakers)

    print("== Numbers of Gaelic speakers ==")
    printTopThree(absoluteSpeakers)

    print()
    print("== Fraction of Gaelic speakers ==")
    printTopThree(relativeSpeakers)

    