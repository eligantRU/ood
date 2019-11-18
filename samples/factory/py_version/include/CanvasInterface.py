from abc import ABC, abstractmethod
from . import *


class ICanvas(ABC):
    @abstractmethod
    def set_color(self, color: Color) -> None:
        pass

    @abstractmethod
    def draw_line(self, start_pos: Vec2, end_pos: Vec2) -> None:
        pass

    @abstractmethod
    def draw_ellipse(self, center: Vec2, radius: Vec2) -> None:
        pass
