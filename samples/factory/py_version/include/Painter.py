from arcade import Window, set_background_color, start_render, run
from include.PainterInterface import IPainter
from include.PictureDraft import PictureDraft
from include.CanvasInterface import ICanvas
from typing import Tuple, Callable


class _Window(Window):
    on_draw_fn = None

    BACKGROUND_COLOR: Tuple[int, int, int] = (0, 0, 0)

    def __init__(self, width: int, height: int, on_draw_fn: Callable[[], None]):
        super().__init__(width, height, "")
        set_background_color(self.BACKGROUND_COLOR)

        self.__on_draw_fn = on_draw_fn

        run()

    def on_draw(self):
        start_render()
        self.__on_draw_fn()


class Painter(IPainter):
    def draw_picture(self, draft: PictureDraft, canvas: ICanvas) -> None:
        draft_width, draft_height = 600, 600
        _Window(draft_width, draft_height, lambda: Painter._draw_picture_impl(draft, canvas))

    @staticmethod
    def _draw_picture_impl(draft: PictureDraft, canvas: ICanvas) -> None:
        for shape in draft.shapes():
            shape.draw(canvas)
