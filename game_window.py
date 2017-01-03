#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, random, settings
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QImage
from timer import Timer
from base_object import BaseObject


class GameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

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
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GameWindow()
    sys.exit(app.exec_())
