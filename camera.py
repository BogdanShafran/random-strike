from rect import Rect


class Camera(Rect):
    def __init__(self):
        super().__init__()
        self.draw_delta_x = 0
        self.draw_delta_y = 0
