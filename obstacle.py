from base_object import BaseObject


class Obstacle(BaseObject):
    def __init__(self, is_destroyable, hit_count_to_destroy):
        self.is_destroyable = is_destroyable
        self.hit_count_to_destroy = hit_count_to_destroy
        self.is_destroyed = False

    def hit(self, hit_power):
        self.hit_count_to_destroy -= hit_power
        if self.is_destroyable and self.hit_count_to_destroy <= 0:
            self.is_destroyed = True
