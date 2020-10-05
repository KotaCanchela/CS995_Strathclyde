class SolarPanel:
    """
    Class that represents a solar panel
    """

    def __init__(self, serialNum, currentPow):
        self.serialNum = serialNum
        self.currentPow = currentPow


class SolarPanelList:
    """
    Class that contains a list of solar panel objects
    """

    def __init__(self, solarList, x, y):
        self.solarList = solarList
        self.x = x
        self.y = y

    def returnPow(self):
        total = 0
        for solarPanel in self.solarList:
            total += solarPanel.currentPow
        return total



if __name__ == "__main__":
    firstSol = SolarPanel(5382, 150)
    secondSol = SolarPanel(5383, 180)
    thirdSol = SolarPanel(6926, 220)
    fourthSol = SolarPanel(8632, 310)

    solarList = [firstSol, secondSol, thirdSol, fourthSol]

    solarPanels = SolarPanelList(solarList, 180, 90)

    print(f"The total power returned from the solar panels is{solarPanels.returnPow()}kWh")
