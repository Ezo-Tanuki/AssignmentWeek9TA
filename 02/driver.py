from circle import Circle
from cylinder import Cylinder

def main():
    test1 = Circle()
    print(test1.toString(), f"Area: {test1.getArea()}", sep='\n')
    print()

    test1.setRadius(2.0)
    test1.setColor("blue")
    print(test1.toString(), f"Area: {test1.getArea()}", sep='\n')
    print()

    test2 = Cylinder()
    print(test2.toString(), f"Area: {test2.getArea()}, Volume: {test2.getVolume()}", sep='\n')
    print()
    
    test2.setRadius(2.0)
    test2.setColor("blue")
    test2.setHeight(2.0)
    print(test2.toString(), f"Area: {test2.getArea()}, Volume: {test2.getVolume()}", sep='\n')



if __name__ == '__main__':
    main()