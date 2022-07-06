import pygame
import constants as c

from .base import BaseState
from elements.sound_effect import SoundEffect


class GameOver(BaseState):
    def __init__(self):
        super(GameOver, self).__init__()
        self.confirm_sound = SoundEffect(c.CONFIRM_SOUND)
        self.title_font = pygame.font.Font(None, 40)
        self.title = self.title_font.render("Game over", True, pygame.Color("white"))
        self.title_rect = self.title.get_rect(center=self.window_rect.center)
        self.instructions = self.font.render("Press space to start a new game, or enter to go to the menu", True,
                                             pygame.Color("White"))
        instructions_center = (self.window_rect.center[0], self.window_rect.center[1] + 150)
        self.instructions_rect = self.instructions.get_rect(center=instructions_center)

    def startup(self, persistent):
        score = persistent["score"]
        self.final_score = self.font.render(f"Your final score was {score} points", True, pygame.Color("white"))
        final_score_center = (self.window_rect.center[0], self.window_rect.center[1] + 50)
        self.final_score_rect = self.final_score.get_rect(center=final_score_center)

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.confirm_sound.play()
                self.next_state = "GAMEPLAY"
                self.done = True

            elif event.key == pygame.K_RETURN:
                self.confirm_sound.play()
                self.next_state = "MENU"
                self.done = True

            elif event.key == pygame.K_ESCAPE:
                self.quit = True

    def draw(self, window):
        window.fill(pygame.Color("black"))
        window.blit(self.title, self.title_rect)
        window.blit(self.final_score, self.final_score_rect)
        window.blit(self.instructions, self.instructions_rect)
