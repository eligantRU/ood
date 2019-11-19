from abc import ABC, abstractmethod
from include.Shapes import Shape


class IShapeFactory(ABC):
	@abstractmethod
	def create_shape(self, line: str) -> Shape:
		pass
