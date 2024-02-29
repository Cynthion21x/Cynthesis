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

    def FROM_CHARGE(charge):

        R = 0
        B = 0
        G = 255

        if charge < 0:

            R = 255 * -(charge)

            G = 255 * (1+charge)

        if charge > 0:

            B = 255 * charge

            G = 255 * (1-charge)

        return pygame.Color(int(R), int(G), int(B))

# Display

SCREEN_NAME = "Particle Simulation"
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 585

FRAME_RATE = 60
CLICK_DELAY = 5

# Universal Constants

ZOOM = 3

class Universe:

    DECEL = 0.5

    REPULSION = 3