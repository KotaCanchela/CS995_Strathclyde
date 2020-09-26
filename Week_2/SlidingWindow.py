def SmoothCurve(windowSize, inputData, smoothedData):

    del smoothedData[:]

    # Fill smoothedData with a copy of input data

    smoothedData += inputData.copy()

    smoothedValue = 0
    nPointsInWindow = 0
    nPoints = len(inputData)

    for point in range(nPoints):

        # Avoid smoothing if there are not enough points
        if point - windowSize < 0:
            continue
        if point + windowSize >= nPoints:
            break

        for i in range(point - windowSize, point + windowSize + 1):
            smoothedValue += inputData[i]
            nPointsInWindow += 1

        smoothedValue /= float(nPointsInWindow)
        # Add smoothed data point to the list
        smoothedData[point] = smoothedValue


if __name__ == "__main__":
    inputData = [
        2.0,
        1.0,
        2.0,
        1.0,
        2.0,
        1.0,
    ]
    smoothedData = []

    SmoothCurve(1, inputData, smoothedData)
    print(f"Input data = {str(inputData)}")
    print(f"Smoothed data = {str(smoothedData)}")
