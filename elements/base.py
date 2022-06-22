import pygame


class BaseObject(pygame.sprite.Sprite):
    def __init__(self):
        super(BaseObject, self).__init__()
        self.x = 0
        self.y = 0
        self.speed_x = 0
        self.speed_y = 0
        self.speed = 0

    def update(self):
        pass

    def draw(self, window):
        pass
