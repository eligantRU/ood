from include.CanvasInterface import ICanvas
from unittest import TestCase, main
from include.Client import Client


class TestClient(TestCase):
	def test_returning_canvas(self):
		self.assertTrue(isinstance(Client.canvas(), ICanvas))

	def test_returning_different_canvases(self):
		self.assertNotEqual(Client.canvas(), Client.canvas())


if __name__ == '__main__':
	main()
