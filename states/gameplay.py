import pygame
from elements import player
from .base import BaseState


class GamePlay(BaseState):
    def __init__(self):
        super(GamePlay, self).__init__()
        self.next_state = "GAMEOVER"
        self.player = player.Player()

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.done = True

    def draw(self, window):
        window.fill(pygame.Color("black"))
        self.player.draw(window)

    def update(self, dt):
        self.player.update()
