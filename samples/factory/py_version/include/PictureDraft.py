from include.Shapes import Shape
from typing import List


class PictureDraft:
    __shapes = None

    def __init__(self, shapes: List[Shape]):
        self.__shapes = shapes

    def shapes(self) -> List[Shape]:
        return self.__shapes
