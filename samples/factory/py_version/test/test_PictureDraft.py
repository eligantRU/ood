from include.Shapes import Triangle, Rectangle
from include.PictureDraft import PictureDraft
from unittest import TestCase, main
from include.Color import Color


class TestPictureDraft(TestCase):
	def test_returning_shapes(self):
		shapes = []
		self.assertListEqual(PictureDraft(shapes).shapes(), shapes)

		shapes = [
			Triangle(Color.RED, (0, 0), (1, 1), (2, 2)),
			Rectangle(Color.RED, (0, 1), (1, 0)),
		]
		self.assertListEqual(PictureDraft(shapes).shapes(), shapes)


if __name__ == '__main__':
	main()
