from include.Shapes import Triangle, Rectangle, Ellipse, RegularPolygon
from include.PictureDraft import PictureDraft
from include.CanvasInterface import ICanvas
from unittest import TestCase, main
from include.Painter import Painter
from include.Color import Color


class _MockCanvas(ICanvas):
	__log = []

	def __init__(self, log):
		self.__log = log

	def set_color(self, color):
		self.__log.append((self.set_color.__name__, color))

	def draw_line(self, start_pos, end_pos):
		self.__log.append((self.draw_line.__name__, start_pos, end_pos))

	def draw_ellipse(self, center, radius):
		self.__log.append((self.draw_ellipse.__name__, center, radius))


class _Painter(Painter):
	def draw_picture(self, draft, canvas):
		self._draw_picture_impl(draft, canvas)


class TestPainter(TestCase):
	def test_should_not_change_canvas_if_draft_is_empty(self):
		log = []

		_Painter().draw_picture(PictureDraft([]), _MockCanvas(log))
		self.assertListEqual(log, [])

	def test_should_paint_in_true_order(self):
		log = []

		_Painter().draw_picture(PictureDraft([
			Triangle(Color.RED, (0, 0), (1, 1), (2, 2)),
			Rectangle(Color.BLACK, (0, 1), (1, 0)),
			Ellipse(Color.GREEN, (3, 14), 15, 92),
			RegularPolygon(Color.YELLOW, (65, 35), 5, 4)
		]), _MockCanvas(log))
		self.assertListEqual(log, [
			('set_color', Color.RED),
			('draw_line', (0, 0), (1, 1)),
			('draw_line', (1, 1), (2, 2)),
			('draw_line', (2, 2), (0, 0)),
			('set_color', Color.BLACK),
			('draw_line', (0, 1), (1, 1)),
			('draw_line', (1, 1), (1, 0)),
			('draw_line', (1, 0), (0, 0)),
			('draw_line', (0, 0), (0, 1)),
			('set_color', Color.GREEN),
			('draw_ellipse', (3, 14), (15, 92)),
			('set_color', Color.YELLOW),
			('draw_line', (70, 35), (65, 40)),
			('draw_line', (65, 40), (60, 35)),
			('draw_line', (60, 35), (65, 30)),
			('draw_line', (65, 30), (70, 35))
		])


if __name__ == '__main__':
	main()
