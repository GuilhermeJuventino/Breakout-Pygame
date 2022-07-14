import asyncio
import pygame, sys
import constants as config

# importing the game states
from states.menu import Menu
from states.gameplay import GamePlay
from states.game_over import GameOver
from states.splash import Splash
from game import Game

# initializing pygame and setting the screen resolution
pygame.init()
window = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Pygame Breakout")

# Game states
states = {
    "MENU": Menu(),
    "SPLASH": Splash(),
    "GAMEPLAY": GamePlay(),
    "GAMEOVER": GameOver(),
}

# Game class instance
game = Game(window, states, "SPLASH")
asyncio.run(game.run())
