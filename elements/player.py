import pygame
import constants as c

from .base import BaseObject


class Player(BaseObject):
    def __init__(self):
        super(Player, self).__init__()
        self.x = 1280 / 2
        self.y = 688
        self.width = 120
        self.height = 27
        self.speed = 5
        self.speed_x = 0
        self.rect = pygame.Rect((0, 0), (self.width, self.height))
        self.rect.center = (self.x, self.y)

    def update(self):
        self.keystate = pygame.key.get_pressed()

        # Handling player movement
        if self.keystate[pygame.K_LEFT] and not self.keystate[pygame.K_RIGHT]:
            self.speed_x = -self.speed

        elif self.keystate[pygame.K_RIGHT] and not self.keystate[pygame.K_LEFT]:
            self.speed_x = self.speed

        else:
            self.speed_x = 0

        self.rect.x += self.speed_x

        # Preventing player from leaving the screen
        if self.rect.right >= c.WIDTH:
            self.rect.right = c.WIDTH

        elif self.rect.left <= 0:
            self.rect.left = 0

    def draw(self, window):
        pygame.draw.rect(window, pygame.Color("white"), self.rect)
