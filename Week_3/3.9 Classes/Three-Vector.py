# Return the azimuthal angle (φ) between the x and y components.
# Return the elevation angle (θ) between the x-y plan and the z axis.
# Return the resultant (r) of the vector

import math

class ThreeVector:
    """
    Class that represents a three-vector
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def azimuthal(self):
        """
        Function that returns the azimuthal angle between the x and y components
        """
        if self.x == 0 and self.y == 0:
            return 0

        return math.atan2(self.y, self.x)

    def elevation(self):
        """
        Function that returns the elevation angle between the x-y plan and the z axis
        """
        if self.x and self.y and self.z == 0:
            return 0

        return math.atan2((math.sqrt(self.x ** self.x + self.y ** self.y)), self.z)

    def resultant(self):
        return math.sqrt((self.x**self.x) + (self.y ** self.y) + (self.z ** self.z))


testRun = ThreeVector(3, 4, 6)


print(testRun.azimuthal())
print(testRun.elevation())
print(testRun.resultant())