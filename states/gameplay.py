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

        # Used to pause the game
        self.paused = False

        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.collide_sprites = pygame.sprite.Group()
        self.block_group = stage_setup(self.all_sprites, self.collide_sprites)

        # Player and ball classes
        self.player = player.Player(self.all_sprites, self.collide_sprites)
        self.ball = ball.Ball(self.all_sprites, self.collide_sprites, self.player)

        # Sprites setup
        self.all_sprites.add(self.player, self.block_group)
        self.collide_sprites.add(self.block_group)

        # Text setup
        self.ui_font = pygame.font.Font(None, 40)
        self.score = self.player.score
        self.score_text = self.ui_font.render(f"Score: {self.score}", True, pygame.Color("White"))
        self.score_rect = self.score_text.get_rect(center=(70, 25))

        self.lives = self.player.lives
        self.lives_text = self.ui_font.render(f"Lives: {self.lives}", True, pygame.Color("White"))
        self.lives_rect = self.lives_text.get_rect(center=(1210, 25))

        self.paused_text = self.font.render(f"Paused", True, pygame.Color("White"))
        self.paused_rect = self.paused_text.get_rect(center=self.window_rect.center)

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                if not self.paused:
                    self.paused = True

                else:
                    self.paused = False

    def startup(self, persistent):
        self.persist["score"] = 0

        # Reseting the player position
        self.player.rect.center = (self.player.x, self.player.y)

        # Reseting the ball's status/position
        self.ball.active = False

        # Reseting the player score
        self.score = 0
        self.player.score = 0

        # Reseting the player's lives
        self.lives = 3
        self.player.lives = 3

        # Reseting the level
        if not self.block_group or self.status == "loser":
            self.all_sprites.empty()
            self.collide_sprites.empty()
            self.block_group.empty()
            self.block_group = stage_setup(self.all_sprites, self.collide_sprites)

            self.all_sprites.add(self.player, self.block_group)
            self.collide_sprites.add(self.block_group)

    def draw(self, window):
        window.fill(pygame.Color("black"))

        # Drawing the game objects
        '''self.player.draw(window)
        self.block_group.draw(window)'''
        self.all_sprites.draw(window)
        self.ball.draw(window)

        # Drawing the ui text
        window.blit(self.score_text, self.score_rect)
        window.blit(self.lives_text, self.lives_rect)

        if self.paused:
            window.blit(self.paused_text, self.paused_rect)

    def update(self, dt):
        if not self.paused:
            # Updating the lives text
            self.lives = self.player.lives
            self.lives_text = self.ui_font.render(f"Lives: {self.lives}", True, pygame.Color("White"))

            # Updating the score text
            self.score = self.player.score
            self.persist["score"] = self.score
            self.score_text = self.ui_font.render(f"Score: {self.score}", True, pygame.Color("White"))

            # Updating the game objects
            '''self.player.update()
            self.block_group.update()'''
            self.all_sprites.update()
            self.ball.update()

            if self.player.lives == 0:
                self.status = "loser"
                self.done = True

            if not self.block_group:
                self.status = "winner"
                self.done = True
