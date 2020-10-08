import csv
import json

def loadData(filename, newData):
    """
    Load json into memory
    """
    del newData[:]
    try:
        with open(filename) as f:
            load = json.load(f)
    except FileNotFoundError:
        return None
    else:
        newData += load


def findMinandMax(newData, dataPoints):
    number_of_rows = len(newData)

    last_pos = 0
    prev_last = 0
    gradient = 0

    for i in range(number_of_rows):
        if i == 0:
            last_pos = newData[i]["distance"]
            continue
        if i == 1:
            prev_last = last_pos
            last_pos = newData[i]["distance"]
            continue

        # Find the gradient sign.
        if last_pos > prev_last:
            gradientSign = 1
        if last_pos < prev_last:
            gradient = -1

        current_pos = newData[i]["distance"]
        if gradient > 0 and last_pos > current_pos:
            dataPoints["TimeStamp"] += [newData[i - 1]["time"]]
            dataPoints["Distance"] += [newData[i - 1]["distance"]]
            dataPoints["InflectionType"] += ["Maximum"]
        elif gradient < 0 and last_pos < current_pos:
            dataPoints["TimeStamp"] += [newData[i - 1]["time"]]
            dataPoints["Distance"] += [newData[i - 1]["distance"]]
            dataPoints["InflectionType"] += ["Minimum"]

        prev_last = last_pos
        last_pos = current_pos

def exportData(filename, data_points):
    """
    Function to export data to CS
    """

    with open(filename, "w") as f:
        csvWriter = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

        # Write the column headings
        column_names = list(data_points.keys())
        csvWriter.writerow(column_names)

        # Write the data columns
        numberof_rows = len(dataPoints[column_names[0]])
        for i in range(numberof_rows):
            outputRow = []
            for columnName in column_names:
                outputRow += [dataPoints[columnName][i]]

            csvWriter.writerow(outputRow)


if __name__ == "__main__":
    newData = []
    loadData("mooninfo_2020.json", newData)

    dataPoints = {}
    dataPoints["TimeStamp"] = []
    dataPoints["InflectionType"] = []
    dataPoints["Distance"] = []

    findMinandMax(newData, dataPoints)

    exportData("maxAndMin.csv", dataPoints)

    loadData("mooninfo_2020.json", newData)