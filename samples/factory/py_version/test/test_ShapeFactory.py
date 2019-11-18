from include.Shapes import Rectangle, Triangle, Ellipse, RegularPolygon
from include.ShapeFactory import ShapeFactory
from unittest import TestCase, main


class TestShapeFactory(TestCase):
	def test_rectangle_creating(self):
		self.assertTrue(isinstance(ShapeFactory().create_shape("rectangle red 100 500 500 100"), Rectangle))

	def test_triangle_creating(self):
		self.assertTrue(isinstance(ShapeFactory().create_shape("triangle blue 500 500 100 400 300 100"), Triangle))

	def test_ellipse_creating(self):
		self.assertTrue(isinstance(ShapeFactory().create_shape("ellipse pink 350 350 50 100"), Ellipse))

	def test_regular_polygon_creating(self):
		self.assertTrue(isinstance(ShapeFactory().create_shape("regular_polygon green 300 300 200 4"), RegularPolygon))

	def test_raise_exception_on_invalid_shape_string(self):
		with self.assertRaises(Exception) as context:
			self.assertTrue(isinstance(ShapeFactory().create_shape("qrectangle red 100 500 500 100"), Rectangle))
		self.assertTrue(isinstance(context.exception, Exception))

	def test_raise_exception_if_no_shape_in_string(self):
		with self.assertRaises(Exception) as context:
			self.assertTrue(isinstance(ShapeFactory().create_shape("hello world"), Rectangle))
		self.assertTrue(isinstance(context.exception, Exception))


if __name__ == '__main__':
	main()
