import pygame

from elements import player, ball
from stage_setup import stage_setup
from .base import BaseState


class GamePlay(BaseState):
    def __init__(self):
        super(GamePlay, self).__init__()
        self.next_state = "GAMEOVER"

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

        # Text setup
        self.score = self.player.score
        self.score_text = self.font.render(f"Score: {self.score}", True, pygame.Color("White"))
        self.score_rect = self.score_text.get_rect(center=(40, 25))

        self.lives = self.player.lives
        self.lives_text = self.font.render(f"Lives: {self.lives}", True, pygame.Color("White"))
        self.lives_rect = self.lives_text.get_rect(center=(1238, 25))

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
        window.blit(self.score_text, self.score_rect)
        window.blit(self.lives_text, self.lives_rect)

    def update(self, dt):
        # Updating the lives text
        self.lives = self.player.lives
        self.lives_text = self.font.render(f"Lives: {self.lives}", True, pygame.Color("White"))

        # Updating the score text
        self.score = self.player.score
        self.score_text = self.font.render(f"Score: {self.score}", True, pygame.Color("White"))

        # Updating the game objects
        self.player.update()
        self.block_group.update()
        self.ball.update()
