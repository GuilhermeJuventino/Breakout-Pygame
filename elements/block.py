import pygame
import constants as c

from .base import BaseObject


class Block(BaseObject):
    def __init__(self, block_type, pos):
        super(Block, self).__init__()
        self.image = pygame.Surface((c.BLOCK_WIDTH, c.BLOCK_HEIGHT))
        self.rect = self.image.get_rect(topleft=pos)
