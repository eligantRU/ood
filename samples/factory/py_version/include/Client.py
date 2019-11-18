from include.CanvasInterface import ICanvas
from include.Canvas import Canvas


class Client:
    @staticmethod
    def canvas() -> ICanvas:
        return Canvas()
