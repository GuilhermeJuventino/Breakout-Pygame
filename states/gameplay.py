import pygame

from elements import player, ball, block as b
from stage_setup import stage_setup
from .base import BaseState


class GamePlay(BaseState):
    def __init__(self):
        super(GamePlay, self).__init__()
        self.next_state = "GAMEOVER"
        self.score = 0

        # Used to determine if the player has lost or won
        self.status = ""

        # Block group
        self.block_group = stage_setup()

        # Player and ball classes
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

            if self.ball.rect.colliderect(block.rect):
                b.damage_block(block)

    def draw(self, window):
        window.fill(pygame.Color("black"))
        self.player.draw(window)
        self.block_group.draw(window)
        self.ball.draw(window)

    def update(self, dt):
        self.player.update()
        self.block_group.update()
        self.ball.update()

        self.handle_collisions()
