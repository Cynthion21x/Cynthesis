import pygame
import os

# Assets Path

ASSETS_PATH = os.path.join(os.path.dirname(__file__), '..', '..', "assets")

# Program Data

DATA_PATH = os.path.join(os.getenv('APPDATA'), '..', 'LocalLow', 'Cynthion21x', 'calcuslugs')

# Colours

class Colours:

    RED = pygame.Color(204, 39, 61)
    BLUE = pygame.Color(38, 50, 181)
    GREEN = pygame.Color(49, 161, 91)

    WHITE = pygame.Color(255, 255, 255)
    BLACK = pygame.Color(0, 0 ,0)

# Display

SCREEN_NAME = "Particle Simulation"
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 585

FRAME_RATE = 60
CLICK_DELAY = 5