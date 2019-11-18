from include.Shapes import Triangle, Rectangle, Ellipse, RegularPolygon
from include.PictureDraft import PictureDraft
from include.CanvasInterface import ICanvas
from unittest import TestCase, main
from include.Painter import Painter
from include.Color import Color


def log_all_methods(log):
	def with_logging(cls, func, log_):
		def wrapper(*args, **kwargs):
			log_.append((cls, func.__name__))
			return func(*args, **kwargs)
		return wrapper

	def decorate(cls):
		for method in [func for func in dir(cls) if callable(getattr(cls, func)) and not func.startswith("__")]:
			if callable(getattr(cls, method)):
				setattr(cls, method, with_logging(cls, getattr(cls, method), log))
		return cls
	return decorate


class _MockCanvas(ICanvas):
	def set_color(self, color):
		pass

	def draw_line(self, start_pos, end_pos):
		pass

	def draw_ellipse(self, center, radius):
		pass


g_log = []


@log_all_methods(g_log)
class LoggingTriangle(Triangle):
	pass


@log_all_methods(g_log)
class LoggingRectangle(Rectangle):
	pass


@log_all_methods(g_log)
class LoggingEllipse(Ellipse):
	pass


@log_all_methods(g_log)
class LoggingRegularPolygon(RegularPolygon):
	pass


class _Painter(Painter):
	def draw_picture(self, draft, canvas):
		self._draw_picture_impl(draft, canvas)


class TestPainter(TestCase):
	def setUp(self):
		global g_log

		g_log.clear()

	def test_should_not_change_canvas_if_draft_is_empty(self):
		global g_log

		_Painter().draw_picture(PictureDraft([]), _MockCanvas())
		self.assertListEqual(g_log, [])

	def test_should_paint_in_true_order(self):
		global g_log

		_Painter().draw_picture(PictureDraft([
			LoggingTriangle(Color.RED, (0, 0), (1, 1), (2, 2)),
			LoggingRectangle(Color.BLACK, (0, 1), (1, 0)),
			LoggingEllipse(Color.GREEN, (3, 14), 15, 92),
			LoggingRegularPolygon(Color.YELLOW, (65, 35), 89, 79)
		]), _MockCanvas())

		self.assertListEqual([value[0] for value in list(filter(lambda value: value[1].startswith("draw"), g_log))], [
			LoggingTriangle,
			LoggingRectangle,
			LoggingEllipse,
			LoggingRegularPolygon,
		])


if __name__ == '__main__':
	main()
