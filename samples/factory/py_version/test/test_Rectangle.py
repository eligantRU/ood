from include.Shapes import Rectangle
from unittest import TestCase, main
from include.Color import Color


class TestRectangle(TestCase):
	def test_cannot_have_left_vertex_larger_than_right_by_horizontal(self):
		with self.assertRaises(Exception) as context:
			Rectangle(Color.RED, (1, 0), (0, 0))
		self.assertTrue(isinstance(context.exception, Exception))

	def test_cannot_have_left_vertex_more_less_than_right_by_vertical(self):
		with self.assertRaises(Exception) as context:
			Rectangle(Color.RED, (0, 0), (0, 1))
		self.assertTrue(isinstance(context.exception, Exception))

	def test_can_return_color(self):
		self.assertEqual(Rectangle(Color.YELLOW, (0, 1), (1, 0)).color(), Color.YELLOW)

	def test_can_return_own_vertices(self):
		rect = Rectangle(Color.RED, (0, 1), (1, 0))

		self.assertTupleEqual(rect.left_top(), (0, 1))
		self.assertTupleEqual(rect.right_bottom(), (1, 0))

	def test_comparison(self):
		rect = Rectangle(Color.RED, (0, 1), (1, 0))
		self.assertEqual(rect, rect)
		self.assertNotEqual(Rectangle(Color.RED, (0, 1), (1, 0)), Rectangle(Color.GREEN, (0, 2), (2, 0)))
		self.assertNotEqual(Rectangle(Color.RED, (0, 1), (1, 0)), None)
		self.assertEqual(Rectangle(Color.RED, (0, 1), (1, 0)), Rectangle(Color.RED, (0, 1), (1, 0)))


if __name__ == '__main__':
	main()
