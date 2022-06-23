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

    def handle_collisions(self):
        self.ball.collide_with(self.player)

        for block in self.block_group:
            self.ball.collide_with(block)

            if self.ball.rect.colliderect(block):
                block.kill()

    def draw(self, window):
        window.fill(pygame.Color("lightblue"))
        self.player.draw(window)
        self.block_group.draw(window)
        self.ball.draw(window)

    def update(self, dt):
        self.player.update()
        self.ball.update()

        self.handle_collisions()
