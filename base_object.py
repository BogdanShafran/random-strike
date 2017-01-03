from PyQt5.QtGui import QImage
from rect import Rect
from geom_utils import is_rect_intersect_rect


class BaseObject(Rect):
    def __init__(self):
        super().__init__()

        self.image = None

    def set_image(self, path):
        self.image = QImage(path)

        self.width = self.image.width()
        self.height = self.image.height()

    def draw(self, painter, camera):
        if is_rect_intersect_rect(self, camera):
            painter.drawImage(int(self.x - camera.x),
                              int(self.y - camera.y),
                              self.image)
