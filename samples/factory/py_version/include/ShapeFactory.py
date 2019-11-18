from include.Shapes import Rectangle, Triangle, Ellipse, RegularPolygon
from include.ShapeFactoryInterface import IShapeFactory
from include.Color import str2color
from include.Shapes import Shape
from typing import Optional
from typing import List


class ShapeFactory(IShapeFactory):
    def create_shape(self, line: str) -> Optional[Shape]:
        args = line.split()

        if not args:
            raise Exception("Shape not found")
        if args[0] == "rectangle":
            shape = self.__process_rectangle(args[1:])
        elif args[0] == "triangle":
            shape = self.__process_triangle(args[1:])
        elif args[0] == "ellipse":
            shape = self.__process_ellipse(args[1:])
        elif args[0] == "regular_polygon":
            shape = self.__process_regular_polygon(args[1:])
        else:
            raise Exception("Unknown shape")
        return shape

    @staticmethod
    def __process_rectangle(args: List[str]) -> Shape:
        if len(args) != 5:
            raise Exception("Invalid shape")
        color = str2color(args[0])
        args = [int(value) for value in args[1:]]
        return Rectangle(color, *zip(args[::2], args[1::2]))

    @staticmethod
    def __process_triangle(args: List[str]) -> Shape:
        if len(args) != 7:
            raise Exception("Invalid shape")
        color = str2color(args[0])
        args = [int(value) for value in args[1:]]
        return Triangle(color, *zip(args[::2], args[1::2]))

    @staticmethod
    def __process_ellipse(args: List[str]) -> Shape:
        if len(args) != 5:
            raise Exception("Invalid shape")
        color = str2color(args[0])
        args = [int(value) for value in args[1:]]
        return Ellipse(color, (args[0], args[1]), args[2], args[3])

    @staticmethod
    def __process_regular_polygon(args: List[str]) -> Shape:
        if len(args) != 5:
            raise Exception("Invalid shape")
        color = str2color(args[0])
        args = [int(value) for value in args[1:]]
        return RegularPolygon(color, (args[0], args[1]), args[2], args[3])
