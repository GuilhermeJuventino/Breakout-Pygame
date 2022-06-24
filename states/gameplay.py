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

        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.collide_sprites = pygame.sprite.Group()
        self.ball_group = pygame.sprite.Group()
        self.block_group = stage_setup(self.all_sprites, self.collide_sprites, self.ball_group)

        # Player and ball classes
        self.player = player.Player(self.all_sprites, self.collide_sprites)
        self.ball = ball.Ball(self.all_sprites, self.collide_sprites, self.player)

        # Sprites setup
        self.all_sprites.add(self.player, self.block_group)
        self.collide_sprites.add(self.block_group)

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.done = True


    def draw(self, window):
        window.fill(pygame.Color("black"))
        self.player.draw(window)
        self.block_group.draw(window)
        self.ball.draw(window)

        '''pygame.draw.rect(window, pygame.Color("red"), self.player.old_rect)
        pygame.draw.rect(window, pygame.Color("white"), self.ball.old_rect)'''

    def update(self, dt):
        self.player.update()
        self.block_group.update()
        self.ball.update()
