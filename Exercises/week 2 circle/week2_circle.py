import math

class Circle():
    """ Circle class that takes radius value and can give diameter and area
    from given radius"""
    def __init__(self, radius=1):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius can't be negative")
        self._radius = radius

    @property
    def diameter(self):
        return 2*self.radius

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter/2


    @property
    def area(self):
        return math.pi*(self.radius**2)

    def __repr__(self):
        return f"Circle({self.radius})"



