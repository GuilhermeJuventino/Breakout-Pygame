import pygame
from .base import BaseState


class Splash(BaseState):
    def __init__(self):
        super(Splash, self).__init__()
        self.title_font = pygame.font.Font(None, 40)
        self.title = self.title_font.render("Pygame Breakout", True, pygame.Color("white"))
        self.title_rect = self.title.get_rect(center=self.window_rect.center)
        self.next_state = "MENU"
        self.time_active = 0

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                self.done = True

    def update(self, dt):
        self.time_active += dt

        if self.time_active >= 5000:
            self.done = True

    def draw(self, window):
        window.fill(pygame.Color("black"))
        window.blit(self.title, self.title_rect)
