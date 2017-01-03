from PyQt5.QtCore import QObject
from base_object import BaseObject
from camera import Camera

class Game:
    def __init__(self, game_window):
        self.game_window = game_window
        game_window.keyPressedAction = self.keyPressEvent
        game_window.paintAction = self.paintAction

    def paintAction(self, painter):
        b = BaseObject()
        b.set_image('res/sample.png')
        b.draw(painter, Camera())

    def keyPressEvent(self, event):
        pass
