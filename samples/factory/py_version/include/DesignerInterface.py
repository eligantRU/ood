from include.PictureDraft import PictureDraft
from fileinput import FileInput
from abc import ABC


class IDesigner(ABC):
    def create_draft(self, stream: FileInput) -> PictureDraft:
        pass
