import pygame
import constants as c

from .base import BaseObject


class Ball(BaseObject):
    def __init__(self):
        super(Ball, self).__init__()
        self.x = c.WIDTH / 2
        self.y = c.HEIGHT / 2
        self.radius = 2
        self.speed_x = 0
        self.speed_y = 0
        self.speed = 5

    def update(self):
        pass

    def draw(self, window):
        pass
