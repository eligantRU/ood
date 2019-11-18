from arcade import draw_line, draw_ellipse_outline
from include.CanvasInterface import ICanvas
from . import *


def color2arcade(color: Color) -> Tuple[int, int, int]:
    if color is Color.BLACK:
        return 192, 192, 192
    elif color is Color.BLUE:
        return 0, 0, 255
    elif color is Color.GREEN:
        return 0, 255, 0
    elif color is Color.RED:
        return 255, 0, 0
    elif color is Color.YELLOW:
        return 249, 166, 2
    elif color is Color.PINK:
        return 255, 20, 147
    raise Exception(f"Unknown color: {color}")


class Canvas(ICanvas):
    __color = None

    def set_color(self, color: Color) -> None:
        self.__color: Color = color

    def draw_line(self, start_pos: Vec2, end_pos: Vec2) -> None:
        start_x, start_y = start_pos
        end_x, end_y = end_pos
        draw_line(start_x, start_y, end_x, end_y, color2arcade(self.__color))

    def draw_ellipse(self, center: Vec2, radius: Vec2) -> None:
        center_x, center_y = center
        horizontal_radius, vertical_radius = radius
        draw_ellipse_outline(center_x, center_y, 2 * horizontal_radius, 2 * vertical_radius, color2arcade(self.__color))
