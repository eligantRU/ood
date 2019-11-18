from unittest import TestCase, main
from include.Shapes import RegularPolygon
from include.Color import Color


class TestRegularPolygon(TestCase):
	def test_radius_cannot_be_negative(self):
		with self.assertRaises(Exception) as context:
			RegularPolygon(Color.BLACK, (0, 1), -2, 3)
		self.assertTrue(isinstance(context.exception, Exception))

	def test_can_return_color(self):
		self.assertEqual(RegularPolygon(Color.BLACK, (0, 1), 2, 3).color(), Color.BLACK)

	def test_can_return_center(self):
		self.assertTupleEqual(RegularPolygon(Color.BLACK, (0, 1), 2, 3).center(), (0, 1))

	def test_can_return_radius(self):
		self.assertEqual(RegularPolygon(Color.BLACK, (0, 1), 2, 3).radius(), 2)

	def test_can_return_reference_vertices_count(self):
		self.assertEqual(RegularPolygon(Color.BLACK, (0, 1), 2, 3).vertex_count(), 3)

	def test_comparison(self):
		polygon = RegularPolygon(Color.BLACK, (0, 1), 2, 3)
		self.assertEqual(polygon, polygon)
		self.assertNotEqual(RegularPolygon(Color.BLACK, (0, 1), 2, 3), RegularPolygon(Color.RED, (1, 2), 3, 4))
		self.assertNotEqual(RegularPolygon(Color.BLACK, (0, 1), 2, 3), None)
		self.assertEqual(RegularPolygon(Color.BLACK, (0, 1), 2, 3), RegularPolygon(Color.BLACK, (0, 1), 2, 3))


if __name__ == '__main__':
	main()
