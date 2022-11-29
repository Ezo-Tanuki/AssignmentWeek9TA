from math import pi as PI

class Circle():
    def __init__(self, radius: float = 1.0, color: str = "red") -> None:
        self.__radius = radius
        self.__color = color

    def getRadius(self) -> float:
        return self.__radius
        
    def setRadius(self, radius: float) -> None:
        self.__radius = radius

    def getColor(self) -> float:
        return self.__color
        
    def setColor(self, color: str) -> None:
        self.__color = color
    
    def toString(self) -> dict:
        return {"class": self.__class__.__name__, "radius": self.__radius, "color": self.__color}

    def getArea(self) -> float:
        return PI * self.__radius ** 2