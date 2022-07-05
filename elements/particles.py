import pygame
import constants as c
from random import randint as rnd

from .base import BaseObject


class Particles(BaseObject):
    def __init__(self, position, direction, color, groups, obstacles, player):
        super(Particles, self).__init__()
        self.position = position
        self.x = self.position[0]
        self.y = self.position[1]

        if direction == "left":
            self.speed_x = rnd(-5, -2)
            self.speed_y = rnd(-2, 2)

        elif direction == "right":
            self.speed_x = rnd(2, 5)
            self.speed_y = rnd(-2, 2)

        if direction == "up":
            self.speed_x = rnd(-2, 2)
            self.speed_y = rnd(-5, -2)

        elif direction == "down":
            self.speed_x = rnd(-1, 1)
            self.speed_y = rnd(2, 5)

        self.color = color
        self.groups = groups
        self.obstacles = obstacles
        self.player = player
        self.lifetime = rnd(8, 19)
        self.radius = rnd(8, 15)
        self.particle_rect = int(self.radius * 2 ** 0.5)
        self.rect = pygame.Rect((self.x, self.y), (self.particle_rect // 2, self.particle_rect // 2))
        self.image = pygame.Surface((self.rect.width, self.rect.height))
        self.image.fill(self.color)
        self.old_rect = self.rect.copy()
        #self.old_image = self.image.copy()

    def update(self):
        # Reducing the particle's radius/lifetime
        self.lifetime -= 1
        self.radius -= 1

        if self.lifetime == 0:
            self.kill()

        # Previous frame
        self.old_rect = self.rect.copy()
        #self.old_image = self.old_image.copy()

        self.rect.x += self.speed_x
        self.collision("horizontal")
        self.collision_window("horizontal")
        self.rect.x = round(self.rect.x)

        self.rect.y += self.speed_y
        self.collision("vertical")
        self.collision_window("vertical")
        self.rect.y = round(self.rect.y)

    def draw(self, window):
        pygame.draw.circle(window, self.color, self.rect.center, self.radius)

    def collision(self, direction):
        collision_sprites = pygame.sprite.spritecollide(self, self.obstacles, False)

        if self.rect.colliderect(self.player.rect):
            collision_sprites.append(self.player)

        if collision_sprites:
            if direction == "horizontal":
                for sprite in collision_sprites:

                    # Collision on the right
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left - 1
                        self.rect.x = self.rect.x
                        self.speed_x *= -1

                    # Collision on the left
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right + 1
                        self.rect.x = self.rect.x
                        self.speed_x *= -1

            if direction == "vertical":
                for sprite in collision_sprites:
                    # Collision on the bottom
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top - 1
                        self.rect.y = self.rect.y
                        self.speed_y *= -1

                    # Collision on the top
                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
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
                self.kill()


class CollisionParticles:
    def __init__(self, position, direction, color, groups, obstacles, player):
        self.position = position
        self.direction = direction
        self.color = color
        self.groups = groups
        self.obstacles = obstacles
        self.player = player
        self.particles = []
        self.amount = rnd(20, 40)

        for i in range(self.amount):
            self.particles.append(Particles(self.position, self.direction,
                                            self.color, self.groups, self.obstacles, self.player))

        self.groups.add(self.particles)

    def draw(self, window):
        for particle in self.particles:
            particle.draw(window)

    def update(self):
        for particle in self.particles:
            particle.update()
