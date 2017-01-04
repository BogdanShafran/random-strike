#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, random, settings
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import pyqtSignal
from timer import Timer
from base_object import BaseObject
from game import Game


class GameWindow(QWidget):
    def __init__(self):
        self.keyPressedAction = None
        self.keyReleasedAction = None
        self.resizeAction = None
        self.paintAction = None

        super().__init__()
        self.initUI()

        self.game = Game(self)

    def initUI(self):
        self.setGeometry(settings.window_x_margin, settings.window_y_margin,
                         settings.window_width, settings.window_height)
        self.setWindowTitle(settings.window_title)

        self.paint_timer = Timer(settings.paint_timer_delay, self.repaint)
        self.paint_timer.start()

        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)

        qp.setBrush(QColor(255, 255, 255))
        qp.drawRect(0, 0, self.width(), self.height())

        if self.paintAction is not None:
            self.paintAction(qp)
        qp.end()

    def keyPressEvent(self, event):
        if self.keyPressedAction is not None:
            self.keyPressedAction(event)

    def keyReleaseEvent(self, event):
        if self.keyReleasedAction is not None:
            self.keyReleasedAction(event)

    def resizeEvent(self, newSize):
        super().resizeEvent(newSize)
        if self.resizeAction is not None:
            self.resizeAction(newSize)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GameWindow()
    sys.exit(app.exec_())
