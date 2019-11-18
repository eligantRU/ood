from include.Designer import Designer
from include.Painter import Painter
from include.Client import Client
from fileinput import input


class Application:
    __client = None
    __painter = None
    __designer = None

    def __init__(self):
        self.__client = Client()
        self.__painter = Painter()
        self.__designer = Designer()

    def run(self) -> None:
        draft = self.__designer.create_draft(input())
        canvas = self.__client.canvas()
        self.__painter.draw_picture(draft, canvas)
