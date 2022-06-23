import pygame

from elements import player, ball
from stage_setup import StageSetup
from .base import BaseState


class GamePlay(BaseState):
    def __init__(self):
        super(GamePlay, self).__init__()
        self.next_state = "GAMEOVER"

        # Block group
        self.block_group = StageSetup()
        self.player = player.Player()
        self.ball = ball.Ball()

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.done = True

    def draw(self, window):
        window.fill(pygame.Color("lightblue"))
        self.player.draw(window)
        self.block_group.draw(window)
        self.ball.draw(window)

    def update(self, dt):
        self.player.update()
        self.ball.update()

        self.ball.collide_with(self.player)
