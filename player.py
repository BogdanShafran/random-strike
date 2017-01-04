import settings
from base_object import BaseObject
from camera import Camera
import geom_utils


class Player(BaseObject):
    def __init__(self):
        self.hp = settings.player_hp
        self.speed = settings.player_speed
        self.camera = Camera()

        self.key_up = None
        self.key_down = None
        self.key_left = None
        self.key_right = None

    def set_camera_position(self, x, y, width, height):
        self.camera.x = x
        self.camera.y = y
        self.camera.width = width
        self.camera.height = height

    def processMove(self, keys, obstacles):
        old_x = self.x
        old_y = self.y
        old_camera_x = self.camera.x
        old_camera_y = self.camera.y

        delta = settings.action_timer_delay / 1000 * self.speed

        for delta_fraction in range(10, 0, -1):
            delta_try = delta * delta_fraction / 10

            if self.key_up in keys:
                self.y -= delta_try
                self.camera.y -= delta_try

            if self.key_down in keys:
                self.y += delta_try
                self.camera.y += delta_try

            if self.key_left in keys:
                self.x -= delta_try
                self.camera.x -= delta_try

            if self.key_right in keys:
                self.x += delta_try
                self.camera.x += delta_try

            success = True
            for obstacle in obstacles:
                if not obstacle.is_destroyed and geom_utils.is_rect_intersect_rect(self, obstacle):
                    self.x = old_x
                    self.y = old_y
                    self.camera.x = old_camera_x
                    self.camera.y = old_camera_y

                    success = False
                    break

            if success:
                break
