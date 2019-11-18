from unittest import TestCase, main
from include.Shapes import Ellipse
from include.Color import Color


class TestEllipse(TestCase):
	def test_both_radius_cannot_be_negative(self):
		with self.assertRaises(Exception) as context:
			Ellipse(Color.BLACK, (0, 1), -2, 3)
		self.assertTrue(isinstance(context.exception, Exception))

		with self.assertRaises(Exception) as context:
			Ellipse(Color.BLACK, (0, 1), 2, -3)
		self.assertTrue(isinstance(context.exception, Exception))

	def test_can_return_color(self):
		self.assertEqual(Ellipse(Color.BLACK, (0, 1), 2, 3).color(), Color.BLACK)

	def test_can_return_center(self):
		self.assertTupleEqual(Ellipse(Color.BLACK, (0, 1), 2, 3).center(), (0, 1))

	def test_can_return_vertical_radius(self):
		self.assertEqual(Ellipse(Color.BLACK, (0, 1), 2, 3).horizontal_radius(), 2)

	def test_can_return_horizontal_radius(self):
		self.assertEqual(Ellipse(Color.BLACK, (0, 1), 2, 3).vertical_radius(), 3)

	def test_comparison(self):
		ellipse = Ellipse(Color.BLACK, (0, 1), 2, 3)
		self.assertEqual(ellipse, ellipse)
		self.assertNotEqual(Ellipse(Color.BLACK, (0, 1), 2, 3), Ellipse(Color.GREEN, (1, 2), 3, 4))
		self.assertNotEqual(Ellipse(Color.BLACK, (0, 1), 2, 3), None)
		self.assertEqual(Ellipse(Color.BLACK, (0, 1), 2, 3), Ellipse(Color.BLACK, (0, 1), 2, 3))


if __name__ == '__main__':
	main()
