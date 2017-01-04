from PyQt5.QtCore import QObject
from PyQt5.QtGui import QColor
from base_object import BaseObject
from camera import Camera
from timer import Timer
import settings
import map

class Game:
    def __init__(self, game_window):
        self.game_window = game_window

        self.load_map()
        self.tune_players()

        self.active_keys = set()

        self.game_window.keyPressedAction = self.keyPressEvent
        self.game_window.keyReleasedAction = self.keyReleaseEvent
        self.game_window.paintAction = self.paintAction
        self.game_window.resizeAction = self.resizeAction

        self.action_timer = Timer(settings.action_timer_delay, self.action)
        self.action_timer.start()

    def action(self):
        for player in self.players:
            player.processMove(self.active_keys, self.obstacles)

    def load_map(self):
        self.players, self.obstacles, self.bonuses = map.load_map(settings.sample_map)
        self.bullets = list()

    def tune_players(self):
        self.tune_players_camera()

        self.players[0].key_up = settings.first_player_up
        self.players[0].key_down = settings.first_player_down
        self.players[0].key_left = settings.first_player_left
        self.players[0].key_right = settings.first_player_right

        self.players[1].key_up = settings.second_player_up
        self.players[1].key_down = settings.second_player_down
        self.players[1].key_left = settings.second_player_left
        self.players[1].key_right = settings.second_player_right

    def tune_players_camera(self):
        width = self.game_window.width()
        height = self.game_window.height()

        self.players[0].camera.width = width / 2
        self.players[0].camera.height = height

        self.players[1].camera.width = width / 2
        self.players[1].camera.height = height

        self.players[0].camera.x = self.players[0].x - width / 4
        self.players[0].camera.y = self.players[0].y - height / 2

        self.players[1].camera.x = self.players[1].x - width / 4
        self.players[1].camera.y = self.players[1].y - height / 2

        self.players[0].camera.draw_delta_x = - settings.camera_divider_width / 2
        self.players[0].camera.draw_delta_y = 0

        self.players[1].camera.draw_delta_x = width / 2 + settings.camera_divider_width / 2
        self.players[1].camera.draw_delta_y = 0

    def paintAction(self, painter):
        #objects
        for camera in (x.camera for x in self.players):
            for player in self.players:
                player.draw(painter, camera)

            for obstacle in self.obstacles:
                obstacle.draw(painter, camera)

            for bonus in self.bonuses:
                bonus.draw(painter, camera)

            for bullet in self.bullets:
                bullet.draw(painter, camera)

        #camera divider
        painter.setBrush(QColor(0, 255, 0))
        painter.drawRect(self.players[0].camera.width,
                         0,
                         settings.camera_divider_width,
                         self.game_window.height())


    def keyPressEvent(self, event):
        self.active_keys.add(event.key())

    def keyReleaseEvent(self, event):
        self.active_keys.remove(event.key())

    def resizeAction(self, newSize):
        self.tune_players_camera()
