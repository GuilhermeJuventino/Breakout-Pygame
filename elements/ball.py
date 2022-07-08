import pygame
import constants as c

from .base import BaseObject
from .block import damage_block
from .particles import CollisionParticles
from.screenshake import ScreenShake
from elements.sound_effect import SoundEffect
from random import randrange as rnd


class Ball(BaseObject):
    def __init__(self, groups, obstacles, player, surf_rect):
        super(Ball, self).__init__()
        self.block_collision_sound = SoundEffect(c.IMPACT_1)
        self.player_collision_sound = SoundEffect(c.IMPACT_2)
        self.shoot_sound = SoundEffect(c.SHOOT_BALL_SOUND)
        self.surf_rect = surf_rect
        self.color = pygame.Color("lightblue")
        self.radius = 12
        self.ball_rect = int(self.radius * 2 ** 0.5)
        self.rect = pygame.Rect(rnd(self.ball_rect, c.WIDTH - self.ball_rect), c.HEIGHT // 2, self.ball_rect, self.ball_rect)
        self.old_rect = self.rect.copy()
        self.speed_x = 0
        self.speed_y = 0
        self.speed = 5
        self.active = False
        self.aim = "right"
        self.groups = groups
        self.obstacles = obstacles
        self.player = player
        self.screen = ScreenShake()

    def update(self):
        # Previous frame
        self.old_rect = self.rect.copy()

        # Current frame (x, y positions)

        if self.active:
            self.rect.x += self.speed_x
            self.collision("horizontal")
            self.collision_window("horizontal")
            self.rect.x = round(self.rect.x)

            self.rect.y += self.speed_y
            self.collision("vertical")
            self.collision_window("vertical")
            self.rect.y = round(self.rect.y)

        if not self.active:
            # Sticking the ball to the player pad
            self.rect.centerx = self.player.rect.centerx
            self.rect.bottom = self.player.rect.top

            # Aiming the ball
            if self.player.keystate[pygame.K_LEFT] and not self.player.keystate[pygame.K_RIGHT]:
                self.aim = "left"

            if self.player.keystate[pygame.K_RIGHT] and not self.player.keystate[pygame.K_LEFT]:
                self.aim = "right"

            # Shooting the ball
            if self.player.keystate[pygame.K_SPACE]:
                self.shoot_sound.play()

                if self.aim == "left":
                    self.speed_x = -self.speed
                    self.speed_y = -self.speed

                elif self.aim == "right":
                    self.speed_x = self.speed
                    self.speed_y = -self.speed

                self.active = True

        self.screen.shake(self.surf_rect)

    def reset_ball(self):
        if self.player.lives > 0:
            self.player.lives -= 1

            if self.player.lives != 0:
                self.active = False

    def draw(self, window):
        pygame.draw.circle(window, (self.color.r, self.color.g, self.color.b), (self.rect.center), self.radius)

    def collision(self, direction):
        collision_sprites = pygame.sprite.spritecollide(self, self.obstacles, False)

        if self.rect.colliderect(self.player.rect):
            self.player_collision_sound.play()
            collision_sprites.append(self.player)

        if collision_sprites:
            if direction == "horizontal":
                for sprite in collision_sprites:
                    if getattr(sprite, 'health', None):
                        self.block_collision_sound.play()
                        self.screen.timer = 15
                        damage_block(sprite)
                        self.player.score += 1

                    # Collision on the right
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.particle = CollisionParticles((sprite.rect.left, self.rect.y), "left", sprite.color,
                                                           self.groups, self.obstacles, self.player)
                        self.rect.right = sprite.rect.left - 1
                        self.rect.x = self.rect.x
                        self.speed_x *= -1

                    # Collision on the left
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.particle = CollisionParticles((sprite.rect.right, self.rect.y), "right", sprite.color,
                                                           self.groups, self.obstacles, self.player)
                        self.rect.left = sprite.rect.right + 1
                        self.rect.x = self.rect.x
                        self.speed_x *= -1


            if direction == "vertical":
                for sprite in collision_sprites:
                    if getattr(sprite, 'health', None):
                        self.block_collision_sound.play()
                        self.screen.timer = 15
                        damage_block(sprite)
                        self.player.score += 1

                    # Collision on the bottom
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.particle = CollisionParticles((self.rect.x, sprite.rect.top), "up", sprite.color,
                                                           self.groups, self.obstacles, self.player)
                        self.rect.bottom = sprite.rect.top - 1
                        self.rect.y = self.rect.y
                        self.speed_y *= -1

                    # Collision on the top
                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.particle = CollisionParticles((self.rect.x, sprite.rect.bottom), "down", sprite.color,
                                                           self.groups, self.obstacles, self.player)
                        self.rect.top = sprite.rect.bottom + 1
                        self.rect.y = self.rect.y
                        self.speed_y *= -1

    def collision_window(self, direction):
        if direction == "horizontal":
            if self.rect.left < 0:
                self.rect.left = 0
                self.rect.x = self.rect.x
                self.speed_x *= -1

            if self.rect.right > c.WIDTH:
                self.rect.right = c.WIDTH
                self.rect.x = self.rect.x
                self.speed_x *= -1

        if direction == "vertical":
            if self.rect.top <= c.TOP_OFFSET:
                self.rect.top = c.TOP_OFFSET
                self.rect.y = self.rect.y
                self.speed_y *= -1

            if self.rect.top > c.HEIGHT:
                self.reset_ball()
