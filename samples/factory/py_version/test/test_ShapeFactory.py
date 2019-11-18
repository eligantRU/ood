from include.Shapes import Rectangle, Triangle, Ellipse, RegularPolygon
from include.ShapeFactory import ShapeFactory
from unittest import TestCase, main
from include.Color import Color


class TestShapeFactory(TestCase):
	def test_rectangle_creating(self):
		self.assertTrue(isinstance(ShapeFactory().create_rectangle(Color.RED, (0, 1), (1, 0)), Rectangle))

	def test_triangle_creating(self):
		self.assertTrue(isinstance(ShapeFactory().create_triangle(Color.BLACK, (0, 0), (1, 1), (2, 2)), Triangle))

	def test_ellipse_creating(self):
		self.assertTrue(isinstance(ShapeFactory().create_ellipse(Color.BLUE, (5, 10), (1, 2)), Ellipse))

	def test_regular_polygon_creating(self):
		self.assertTrue(isinstance(ShapeFactory().create_regular_polygon(Color.YELLOW, (5, 10), 5, 8), RegularPolygon))


if __name__ == '__main__':
	main()
