import pygame
import constants as c

from .base import BaseState
from elements.sound_effect import SoundEffect


class GameOver(BaseState):
    def __init__(self):
        super(GameOver, self).__init__()
        self.confirm_sound = SoundEffect(c.CONFIRM_SOUND)
        self.title_font = pygame.font.Font(None, 40)
        self.persistent_info = {}

        if not self.persistent_info or self.persistent_info["status"] == "loser":
            self.title = self.title_font.render("Game over", True, pygame.Color("white"))
            self.title_rect = self.title.get_rect(center=self.window_rect.center)

            self.instructions = self.font.render("Press space to start a new game, or enter to go to the menu", True,
                                                     pygame.Color("White"))
            instructions_center = (self.window_rect.center[0], self.window_rect.center[1] + 150)
            self.instructions_rect = self.instructions.get_rect(center=instructions_center)


    def startup(self, persistent):
        self.persistent_info["score"] = persistent["score"]
        self.persistent_info["status"] = persistent["status"]
        self.persistent_info["level"] = persistent["level"]

        if self.persistent_info["status"] == "loser":
            self.title = self.title_font.render("Game over", True, pygame.Color("white"))
            self.title_rect = self.title.get_rect(center=self.window_rect.center)

            self.final_score = self.font.render(f"Your final score was {self.persistent_info['score']} points",
                                                True, pygame.Color("white"))
            final_score_center = (self.window_rect.center[0], self.window_rect.center[1] + 50)
            self.final_score_rect = self.final_score.get_rect(center=final_score_center)

            self.instructions = self.font.render("Press space to start a new game, or enter to go to the menu", True,
                                                 pygame.Color("White"))
            instructions_center = (self.window_rect.center[0], self.window_rect.center[1] + 150)
            self.instructions_rect = self.instructions.get_rect(center=instructions_center)

        if self.persistent_info["status"] == "winner":
            self.title = self.title_font.render(f"Level {self.persistent_info['level']} complete",
                                                True, pygame.Color("white"))
            self.title_rect = self.title.get_rect(center=self.window_rect.center)

            self.final_score = self.font.render(f"Your score is {self.persistent_info['score']} points",
                                                True, pygame.Color("white"))
            final_score_center = (self.window_rect.center[0], self.window_rect.center[1] + 50)
            self.final_score_rect = self.final_score.get_rect(center=final_score_center)

            self.instructions = self.font.render("Press space to go to the next level, or enter to go to the menu",
                                                 True,
                                                 pygame.Color("White"))

            instructions_center = (self.window_rect.center[0], self.window_rect.center[1] + 150)
            self.instructions_rect = self.instructions.get_rect(center=instructions_center)

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.confirm_sound.play()
                self.next_state = "GAMEPLAY"
                self.persist["reset"] = False
                self.done = True

            elif event.key == pygame.K_RETURN:
                self.confirm_sound.play()
                self.persist["reset"] = True
                self.next_state = "MENU"
                self.done = True

            elif event.key == pygame.K_ESCAPE:
                self.quit = True

    def draw(self, window):
        window.fill(pygame.Color("black"))
        window.blit(self.title, self.title_rect)
        window.blit(self.final_score, self.final_score_rect)
        window.blit(self.instructions, self.instructions_rect)
