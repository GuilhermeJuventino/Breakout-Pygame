import pygame
from .base import BaseState


class GameOver(BaseState):
    def __init__(self):
        super(GameOver, self).__init__()
        self.title = self.font.render("Game over", True, pygame.Color("white"))
        self.title_rect = self.title.get_rect(center=self.window_rect.center)
        self.instructions = self.font.render("Press space to start a new game, or enter to go to the menu", True,
                                             pygame.Color("White"))
        instructions_center = (self.window_rect.center[0], self.window_rect.center[1] + 50)
        self.instructions_rect = self.instructions.get_rect(center=instructions_center)

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.next_state = "GAMEPLAY"
                self.done = True

            elif event.key == pygame.K_RETURN:
                self.next_state = "MENU"
                self.done = True

            elif event.key == pygame.K_ESCAPE:
                self.quit = True

    def draw(self, window):
        window.fill(pygame.Color("black"))
        window.blit(self.title, self.title_rect)
        window.blit(self.instructions, self.instructions_rect)
