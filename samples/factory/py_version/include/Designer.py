from include.PictureDraft import PictureDraft as PictureDraft_
from include.ShapeFactory import ShapeFactory as ShapeFactory_
from include.DesignerInterface import IDesigner
from include.Color import str2color
from include.Shapes import Shape
from fileinput import FileInput
from typing import Optional
from typing import List


class Designer(IDesigner):
    def create_draft(self, stream: FileInput) -> PictureDraft_:
        with stream:
            return PictureDraft_(list(filter(lambda shape: shape, [Designer.__process(line) for line in stream])))

    @staticmethod
    def __process(command: str) -> Optional[Shape]:
        factory = ShapeFactory_()

        args = command.split()

        shape = None
        try:
            if not args:
                raise Exception("Shape not found")
            if args[0] == "rectangle":
                shape = Designer.__process_rectangle(factory, args[1:])
            elif args[0] == "triangle":
                shape = Designer.__process_triangle(factory, args[1:])
            elif args[0] == "ellipse":
                shape = Designer.__process_ellipse(factory, args[1:])
            elif args[0] == "regular_polygon":
                shape = Designer.__process_regular_polygon(factory, args[1:])
            else:
                raise Exception("Unknown shape")
        except Exception as ex:
            print(ex)
        return shape

    @staticmethod
    def __process_triangle(factory: ShapeFactory_, args: List[str]) -> Shape:
        if len(args) != 7:
            raise Exception("Invalid shape")
        color = str2color(args[0])
        args = [float(value) for value in args[1:]]
        return factory.create_triangle(color, *zip(args[::2], args[1::2]))

    @staticmethod
    def __process_rectangle(factory: ShapeFactory_, args: List[str]) -> Shape:
        if len(args) != 5:
            raise Exception("Invalid shape")
        color = str2color(args[0])
        args = [float(value) for value in args[1:]]
        return factory.create_rectangle(color, *zip(args[::2], args[1::2]))

    @staticmethod
    def __process_ellipse(factory: ShapeFactory_, args: List[str]) -> Shape:
        if len(args) != 5:
            raise Exception("Invalid shape")
        color = str2color(args[0])
        args = [float(value) for value in args[1:]]
        return factory.create_ellipse(color, *zip(args[::2], args[1::2]))

    @staticmethod
    def __process_regular_polygon(factory: ShapeFactory_, args: List[str]) -> Shape:
        if len(args) != 5:
            raise Exception("Invalid shape")
        color = str2color(args[0])
        args = [int(value) for value in args[1:]]
        return factory.create_regular_polygon(color, (args[0], args[1]), args[2], args[3])
