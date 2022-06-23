import pygame
import constants as c

from .base import BaseObject
from random import randrange as rnd

class Ball(BaseObject):
    def __init__(self):
        super(Ball, self).__init__()
        self.x = c.WIDTH / 2
        self.y = c.HEIGHT / 2
        self.radius = 12
        self.ball_rect = int(self.radius * 2 ** 0.5)
        self.rect = pygame.Rect(rnd(self.ball_rect, c.WIDTH - self.ball_rect), c.HEIGHT // 2, self.ball_rect, self.ball_rect)
        self.speed_x = 5
        self.speed_y = 5

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0 or self.rect.right >= c.WIDTH:
            self.speed_x *= -1

        if self.rect.top <= 0 or self.rect.bottom >= c.HEIGHT:
            self.speed_y *= -1

    def draw(self, window):
        pygame.draw.circle(window, pygame.Color("blue"), (self.rect.center), self.radius)

    def collide_with(self, target):
        pass
