import pygame

from elements.sound_effect import SoundEffect
import constants as c

from.base import BaseState


class Credits(BaseState):
    def __init__(self):
        super(Credits, self).__init__()
        self.confirm_sound = SoundEffect(c.CONFIRM_SOUND)
        self.title_font = pygame.font.Font(None, 40)
        self.persistent_info = {}

        self.title = self.title_font.render("Congratulations, you've beaten the game!",
                                                True, pygame.Color("white"))
        self.title_rect = self.title.get_rect(center=self.window_rect.center)

        self.credits = self.font.render("Pygame Breakout made by Guilherme Juventino using PyGame",
                                                True, pygame.Color("white"))
        credits_center = (self.window_rect.center[0], self.window_rect.center[1] + 150)
        self.credits_rect = self.credits.get_rect(center=credits_center)

        self.instructions = self.font.render("Press space to start a new game, or enter to go to the menu", True,
                                             pygame.Color("White"))
        instructions_center = (self.window_rect.center[0], self.window_rect.center[1] + 200)
        self.instructions_rect = self.instructions.get_rect(center=instructions_center)

    def startup(self, persistent):
        self.persistent_info["score"] = persistent["score"]

        self.final_score = self.font.render(f"Your final score was {self.persistent_info['score']} points",
                                            True, pygame.Color("white"))
        final_score_center = (self.window_rect.center[0], self.window_rect.center[1] + 50)
        self.final_score_rect = self.final_score.get_rect(center=final_score_center)

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.confirm_sound.play()
                self.next_state = "GAMEPLAY"
                self.persist["reset"] = True
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
        window.blit(self.credits, self.credits_rect)
        window.blit(self.final_score, self.final_score_rect)
        window.blit(self.instructions, self.instructions_rect)
