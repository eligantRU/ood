from include.PictureDraft import PictureDraft
from include.CanvasInterface import ICanvas
from abc import ABC


class IPainter(ABC):
    def draw_picture(self, draft: PictureDraft, canvas: ICanvas) -> None:
        pass
