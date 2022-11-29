from circle import Circle

class Cylinder(Circle):
    def __init__(self, height: float = 1.0, radius: float = 1.0, color: str = "red"):
        self.__height = height
        super().__init__(radius, color)

    def getHeight(self) -> float:
        return self.__height

    def setHeight(self, height: float) -> None:
        self.__height = height

    def toString(self):
        dic = super().toString()
        dic.update({"height": self.__height})
        return dic

    def getVolume(self) -> float:
        return self.getArea() * self.__height