from include.Shapes import Rectangle, Triangle, Ellipse, RegularPolygon
from include.ShapeFactory import ShapeFactory
from include.Designer import Designer
from unittest import TestCase, main
from include.Color import Color
from fileinput import FileInput


class _MockFileInput(FileInput):
	__current_line = None
	__lines = None

	def __init__(self, lines):
		super().__init__()

		self.__lines, self.__current_line = lines, 0

	def __del__(self):
		pass

	def close(self):
		raise NotImplementedError

	def __enter__(self):
		return self

	def __exit__(self, type_, value, traceback):
		pass

	def __iter__(self):
		return self

	def __next__(self):
		if self.__current_line == len(self.__lines):
			raise StopIteration
		line = self.__lines[self.__current_line]
		self.__current_line += 1
		return line

	def __getitem__(self, i):
		if i != self.lineno():
			raise RuntimeError("accessing lines out of order")
		try:
			return self.__next__()
		except StopIteration:
			raise IndexError("end of input reached")

	def nextfile(self):
		raise NotImplementedError

	def readline(self):
		raise NotImplementedError

	def filename(self):
		raise NotImplementedError

	def lineno(self):
		raise NotImplementedError

	def filelineno(self):
		raise NotImplementedError

	def fileno(self):
		raise NotImplementedError

	def isfirstline(self):
		raise self.__current_line == 1

	def isstdin(self):
		raise NotImplementedError


class TestDesigner(TestCase):
	def test_return_empty_draft_if_there_r_no_shapes_in_input(self):
		self.assertListEqual(Designer(ShapeFactory()).create_draft(_MockFileInput([])).shapes(), [])

	def test_return_nonempty_draft_if_there_r_shapes_in_input(self):
		shapes = Designer(ShapeFactory()).create_draft(_MockFileInput([
			"rectangle red 100 500 500 100",
			"rectangle black 250 400 350 200",
			"triangle blue 500 500 100 400 300 100",
			"triangle black 100 100 300 500 500 100",
			"ellipse pink 350 350 50 100",
			"ellipse blue 300 300 200 200",
			"regular_polygon green 300 300 200 4",
			"regular_polygon yellow 300 300 200 8",
		])).shapes()

		self.assertListEqual(shapes, [
			Rectangle(Color.RED, (100, 500), (500, 100)),
			Rectangle(Color.BLACK, (250, 400), (350, 200)),
			Triangle(Color.BLUE, (500, 500), (100, 400), (300, 100)),
			Triangle(Color.BLACK, (100, 100), (300, 500), (500, 100)),
			Ellipse(Color.PINK, (350, 350), 50, 100),
			Ellipse(Color.BLUE, (300, 300), 200, 200),
			RegularPolygon(Color.GREEN, (300, 300), 200, 4),
			RegularPolygon(Color.YELLOW, (300, 300), 200, 8),
		])

	def test_forgive_mistakes_in_input(self):
		shapes = Designer(ShapeFactory()).create_draft(_MockFileInput([
			"rerctangle red 100 500 500 100",
			"rectangle reda 100 500 500 100",
			"rectangle red abc 500 500 100",
			"hello world",
			"",
			"rectangle black 250 400 350 200",
			"The Hell designed by JS",
			"triangqle blue 500 500 100 400 300 100",
			"triangle lue 500 500 100 400 300 100",
			"triangle blue abc 500 100 400 300 100",
			"The Hell designed by JS",
			"triangle blue 500 500 100 400 300 100",
			"eqllipse pink 350 350 50 100",
			"ellipse punk 350 350 50 100",
			"ellipse pink abc 350 50 100",
			"The Hell designed by JS",
			"ellipse pink 350 350 50 100",
			"regular_ponygon green 300 300 200 4",
			"regular_polygon queen 300 300 200 4",
			"regular_polygon green abc 300 200 4",
			"regular_polygon green 300 300 200 4",
			"",
		])).shapes()

		self.assertListEqual(shapes, [
			Rectangle(Color.BLACK, (250, 400), (350, 200)),
			Triangle(Color.BLUE, (500, 500), (100, 400), (300, 100)),
			Ellipse(Color.PINK, (350, 350), 50, 100),
			RegularPolygon(Color.GREEN, (300, 300), 200, 4),
		])


if __name__ == '__main__':
	main()
