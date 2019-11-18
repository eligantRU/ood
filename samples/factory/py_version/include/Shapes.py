from include.CanvasInterface import ICanvas
from abc import ABC, abstractmethod
from math import pi, sin, cos
from numpy import arange
from . import *


class Shape(ABC):
	__color = None

	def __init__(self, color: Color):
		super().__init__()

		self.__color = color

	def color(self) -> Color:
		return self.__color

	@abstractmethod
	def draw(self, canvas: ICanvas) -> None:
		pass


class Rectangle(Shape):
	__left_top, __right_bottom = None, None

	def __init__(self, color: Color, left_top: Vec2, right_bottom: Vec2):
		super().__init__(color)

		if left_top[0] > right_bottom[0]:
			raise Exception("Rectangle must have left vertex more less than right by horizontal")
		if left_top[1] < right_bottom[1]:
			raise Exception("Rectangle must have left vertex larger than right by vertical")

		self.__left_top, self.__right_bottom = left_top, right_bottom

	def draw(self, canvas: ICanvas) -> None:
		canvas.set_color(self.color())
		canvas.draw_line(self.__left_top, (self.__right_bottom[0], self.__left_top[1]))
		canvas.draw_line((self.__right_bottom[0], self.__left_top[1]), self.__right_bottom)
		canvas.draw_line(self.__right_bottom, (self.__left_top[0], self.__right_bottom[1]))
		canvas.draw_line((self.__left_top[0], self.__right_bottom[1]), self.__left_top)

	def left_top(self) -> Vec2:
		return self.__left_top

	def right_bottom(self) -> Vec2:
		return self.__right_bottom

	def __eq__(self, other) -> bool:
		return isinstance(other, Rectangle) \
				and self.color() is other.color() \
				and self.__left_top == other.left_top() \
				and self.__right_bottom == other.right_bottom()


class Triangle(Shape):
	__vertex1, __vertex2, __vertex3 = None, None, None

	def __init__(self, color: Color, vertex1: Vec2, vertex2: Vec2, vertex3: Vec2):
		super().__init__(color)

		self.__vertex1, self.__vertex2, self.__vertex3 = vertex1, vertex2, vertex3

	def draw(self, canvas: ICanvas) -> None:
		canvas.set_color(self.color())
		canvas.draw_line(self.__vertex1, self.__vertex2)
		canvas.draw_line(self.__vertex2, self.__vertex3)
		canvas.draw_line(self.__vertex3, self.__vertex1)

	def vertex1(self) -> Vec2:
		return self.__vertex1

	def vertex2(self) -> Vec2:
		return self.__vertex2

	def vertex3(self) -> Vec2:
		return self.__vertex3

	def __eq__(self, other) -> bool:
		return isinstance(other, Triangle) \
				and self.color() is other.color() \
				and self.__vertex1 == other.vertex1() \
				and self.__vertex2 == other.vertex2() \
				and self.__vertex3 == other.vertex3()


class Ellipse(Shape):
	__horizontal_radius, __vertical_radius = None, None
	__center = None

	def __init__(self, color: Color, center: Vec2, horizontal_radius: int, vertical_radius: int):
		super().__init__(color)

		if not all([radius > 0 for radius in [vertical_radius, horizontal_radius]]):
			raise Exception("Radius cannot be negative")

		self.__center = center
		self.__horizontal_radius, self.__vertical_radius = horizontal_radius, vertical_radius

	def draw(self, canvas: ICanvas) -> None:
		canvas.set_color(self.color())
		canvas.draw_ellipse(self.__center, (self.__horizontal_radius, self.__vertical_radius))

	def center(self) -> Vec2:
		return self.__center

	def horizontal_radius(self) -> int:
		return self.__horizontal_radius

	def vertical_radius(self) -> int:
		return self.__vertical_radius

	def __eq__(self, other) -> bool:
		return isinstance(other, Ellipse) \
				and self.color() is other.color() \
				and self.__center == other.center() \
				and self.__horizontal_radius == other.horizontal_radius() \
				and self.__vertical_radius == other.vertical_radius()


class RegularPolygon(Shape):
	__radius = None
	__center = None
	__vertex_count = None

	def __init__(self, color: Color, center: Vec2, radius: int, vertex_count: int):
		super().__init__(color)

		if radius < 0:
			raise Exception("Radius cannot be negative")

		self.__center = center
		self.__radius = radius
		self.__vertex_count = vertex_count

	def draw(self, canvas: ICanvas) -> None:
		eps = 1e-4
		step = 2 * pi / self.__vertex_count
		points = []

		center_x, center_y = self.__center
		for angle in arange(0, 2 * pi, step):
			alpha = 0 if abs(angle - 2 * pi) < eps else angle
			dx = self.__radius * cos(alpha)
			dy = self.__radius * sin(alpha)
			points.append((int(center_x + dx), int(center_y + dy)))
		points.append(points[0])

		canvas.set_color(self.color())
		for i in range(0, len(points) - 1):
			canvas.draw_line(points[i], points[i + 1])

	def center(self) -> Vec2:
		return self.__center

	def radius(self) -> int:
		return self.__radius

	def vertex_count(self) -> int:
		return self.__vertex_count

	def __eq__(self, other) -> bool:
		return isinstance(other, RegularPolygon) \
				and self.color() is other.color() \
				and self.__center == other.center() \
				and self.__radius == other.radius() \
				and self.__vertex_count == self.vertex_count()
