import pygame
import constants as c

from .base import BaseObject


class Block(BaseObject):
    def __init__(self, block_type, pos):
        super(Block, self).__init__()
        self.type = block_type
        self.health = int(self.type)
        self.color = c.COLOR_LEGEND[self.type]
        self.image = pygame.Surface((c.BLOCK_WIDTH, c.BLOCK_HEIGHT))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        self.color = c.COLOR_LEGEND[self.type]
        self.image.fill(self.color)

    def draw(self, window):
        pygame.draw.rect(window, pygame.Color(self.color), self.rect)


def damage_block(block):
    if block.health > 0:
        block.health -= 1
        block.type = str(block.health)

    if block.health == 0:
        block.kill()
