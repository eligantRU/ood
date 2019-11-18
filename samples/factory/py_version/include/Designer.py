from include.PictureDraft import PictureDraft as PictureDraft_
from include.ShapeFactory import ShapeFactory as ShapeFactory_
from include.DesignerInterface import IDesigner
from fileinput import FileInput


class Designer(IDesigner):
    __shape_factory = None

    def __init__(self, shape_factory: ShapeFactory_):
        super().__init__()

        self.__shape_factory = shape_factory

    def create_draft(self, stream: FileInput) -> PictureDraft_:
        with stream:
            shapes = []
            for line in stream:
                try:
                    shapes.append(self.__shape_factory.create_shape(line))
                except Exception as ex:
                    print(ex)
            return PictureDraft_(shapes)
