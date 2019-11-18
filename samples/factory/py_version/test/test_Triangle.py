from unittest import TestCase, main
from include.Shapes import Triangle
from include.Color import Color


class TestTriangle(TestCase):
	def test_can_return_color(self):
		self.assertEqual(Triangle(Color.RED, (0, 1), (2, 3), (4, 5)).color(), Color.RED)

	def test_can_return_own_vertices(self):
		triangle = Triangle(Color.RED, (0, 1), (2, 3), (4, 5))

		self.assertTupleEqual(triangle.vertex1(), (0, 1))
		self.assertTupleEqual(triangle.vertex2(), (2, 3))
		self.assertTupleEqual(triangle.vertex3(), (4, 5))

	def test_comparison(self):
		triangle = Triangle(Color.RED, (0, 1), (2, 3), (4, 5))
		self.assertEqual(triangle, triangle)
		self.assertNotEqual(Triangle(Color.RED, (0, 1), (2, 3), (4, 5)), Triangle(Color.PINK, (1, 2), (3, 4), (5, 6)))
		self.assertNotEqual(Triangle(Color.RED, (0, 1), (2, 3), (4, 5)), None)
		self.assertEqual(Triangle(Color.RED, (0, 1), (2, 3), (4, 5)), Triangle(Color.RED, (0, 1), (2, 3), (4, 5)))


if __name__ == '__main__':
	main()
