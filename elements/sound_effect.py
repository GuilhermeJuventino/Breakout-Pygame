import pygame


class SoundEffect:
    def __init__(self, path):
        self.sound = pygame.mixer.Sound(path)

    def play(self, volume=5):
        self.sound.set_volume(volume)
        self.sound.play()
