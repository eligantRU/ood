from include.Shapes import Shape, Rectangle, Triangle, Ellipse, RegularPolygon
from . import *


class ShapeFactory:
    @staticmethod
    def create_rectangle(color: Color, left_top: Vec2, right_bottom: Vec2) -> Shape:
        return Rectangle(color, left_top, right_bottom)

    @staticmethod
    def create_triangle(color: Color, vertex1: Vec2, vertex2: Vec2, vertex3: Vec2) -> Shape:
        return Triangle(color, vertex1, vertex2, vertex3)

    @staticmethod
    def create_ellipse(color: Color, center: Vec2, radius: Vec2) -> Shape:
        return Ellipse(color, center, *radius)

    @staticmethod
    def create_regular_polygon(color: Color, center: Vec2, radius: int, vertex_count: int) -> Shape:
        return RegularPolygon(color, center, radius, vertex_count)
