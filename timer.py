import settings
from PyQt5.QtCore import QBasicTimer, QObject

class Timer(QObject):
    def __init__(self, delay, action):
        super().__init__()

        self.timer = QBasicTimer()
        self.delay = delay
        self.action = action

    def timerEvent(self, e):
        self.action()

    def start(self):
        self.timer.start(self.delay, self)

    def stop(self):
        self.timer.stop()
