
from dataclasses import dataclass

@dataclass
class Rectangle:
    height: int
    width: int

    def perimeter(self):
        return (self.height * 2) + (self.width * 2)

    def area(self):
        return self.height * self.width

    def rectangle_string(self):
        height = self.height
        width = self.width

        if height == 1:
            print("* " * width)
        else:
            print("* " * width)
            for i in range(height - 2):
                print("*" + " " * (width * 2 - 3) + "*")
            print("* " * width)

def main():
    print("Rectangle Calculator")
    print()

    choice = "y"
    while choice.lower() == "y":
        height = int(input("Height: "))
        width = int(input("Width: "))

        rectangle = Rectangle(height, width)
        perimeter = rectangle.perimeter()
        area = rectangle.area()

        print(f"Perimeter: {perimeter}")
        print(f"Area: {area}")
        rectangle.rectangle_string()
        print()

        choice = input("Continue? (y/n) ")
        print()

if __name__ == "__main__":
    main()