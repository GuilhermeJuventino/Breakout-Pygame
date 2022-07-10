import pygame
import constants as c

from .base import BaseState
from elements.sound_effect import SoundEffect


class Menu(BaseState):
    def __init__(self):
        super(Menu, self).__init__()
        self.navigation_sound = SoundEffect(c.NAVIGATION_SOUND)
        self.confirm_sound = SoundEffect(c.CONFIRM_SOUND)
        self.active_index = 0
        self.options = ["Start game", "Quit game"]
        self.next_state = "GAMEPLAY"
        self.level = 1

    def render_text(self, index):
        color = pygame.Color("red") if index == self.active_index else pygame.Color("white")
        return self.font.render(self.options[index], True, color)

    def get_text_position(self, text, index):
        center = (self.window_rect.center[0], self.window_rect.center[1] + index * 50)
        return text.get_rect(center=center)

    def handle_action(self):
        if self.active_index == 0:
            self.confirm_sound.play()
            self.done = True

        elif self.active_index == 1:
            self.quit = True

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.active_index = 1 if self.active_index <= 0 else 0
                self.navigation_sound.play()

            elif event.key == pygame.K_DOWN:
                self.active_index = 0 if self.active_index >= 1 else 1
                self.navigation_sound.play()

            elif event.key == pygame.K_RETURN:
                self.handle_action()

    def draw(self, window):
        window.fill(pygame.Color("black"))

        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            window.blit(text_render, self.get_text_position(text_render, index))
