import pygame
import constants as c

from elements import player, ball
from elements.sound_effect import SoundEffect
from elements.particles import StarField
from stage_setup import stage_setup
from .base import BaseState


class GamePlay(BaseState):
    def __init__(self):
        super(GamePlay, self).__init__()
        self.level = 1
        self.next_state = "GAMEOVER"
        self.reset = False

        self.pause_sound = SoundEffect(c.CONFIRM_SOUND)

        # Used to determine if the player has lost or won
        self.status = ""

        # Used to pause the game
        self.paused = False

        self.main_surface = pygame.Surface((c.WIDTH, c.HEIGHT))
        self.main_rect = self.main_surface.get_rect()

        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.collide_sprites = pygame.sprite.Group()
        self.block_group = stage_setup(self.all_sprites, self.collide_sprites)

        # Classes
        self.player = player.Player(self.all_sprites, self.collide_sprites)
        self.ball = ball.Ball(self.all_sprites, self.collide_sprites, self.player, self.main_rect)
        self.star_field = StarField()

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
                self.pause_sound.play()
                if not self.paused:
                    self.paused = True

                else:
                    self.paused = False

    def startup(self, persistent):
        self.persist["score"] = 0

        if persistent:
            self.reset = persistent["reset"]

        # Reseting the player position
        self.player.rect.center = (self.player.x, self.player.y)

        # Reseting the ball's status/position
        self.ball.active = False

        if self.status == "loser" or self.reset:
            # Reseting the player score
            self.score = 0
            self.player.score = 0

            # Reseting the player's lives
            self.lives = 3
            self.player.lives = 3

            self.level = 1

        # Reseting the level
        if not self.block_group or self.status == "loser":
            self.all_sprites.empty()
            self.collide_sprites.empty()
            self.block_group.empty()
            self.star_field.stars.clear()
            self.block_group = stage_setup(self.all_sprites, self.collide_sprites, self.level)

            self.all_sprites.add(self.player, self.block_group)
            self.collide_sprites.add(self.block_group)

    def draw(self, window):
        window.fill(pygame.Color("black"))

        window.blit(self.main_surface, self.main_rect)

        self.main_surface.fill(pygame.Color("black"))

        # Drawing the game objects
        self.star_field.draw(self.main_surface)
        self.all_sprites.draw(self.main_surface)
        self.ball.draw(self.main_surface)

        # Drawing the ui text
        window.blit(self.score_text, self.score_rect)
        window.blit(self.lives_text, self.lives_rect)

        if self.paused:
            window.blit(self.paused_text, self.paused_rect)

    def update(self, dt):
        if not self.paused:
            # Reseting main_surface to default position (required for screenshake)
            self.main_rect.topleft = (0, 0)

            # Updating the lives text
            self.lives = self.player.lives
            self.lives_text = self.ui_font.render(f"Lives: {self.lives}", True, pygame.Color("White"))

            # Updating the score text
            self.score = self.player.score
            self.persist["score"] = self.score
            self.score_text = self.ui_font.render(f"Score: {self.score}", True, pygame.Color("White"))

            # Updating the game objects
            self.star_field.update()
            self.all_sprites.update()
            self.ball.update()

            if self.player.lives == 0:
                self.status = "loser"
                self.persist["status"] = self.status
                self.level = 1
                self.persist["level"] = self.level
                self.done = True

            if not self.block_group:
                self.status = "winner"
                self.persist["status"] = self.status
                self.persist["level"] = self.level

                self.level += 1

                if self.level <= c.FINAL_LEVEL:
                    self.next_state = "GAMEOVER"
                    self.done = True

                elif self.level > c.FINAL_LEVEL:
                    self.next_state = "CREDITS"
                    self.done = True
