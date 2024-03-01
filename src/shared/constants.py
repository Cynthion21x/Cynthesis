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

        R = (255, 0, 128)
        P = (128, 0, 255)
        G = (10, 255, 10)

        normC = charge + 1

        Red = 0
        Green = 0
        Blue = 0

        if (normC < 1):

            Red += (R[0] / 2) * (2-normC)
            Green += (R[1] / 2) * (2-normC)
            Blue += (R[2] / 2) * (2-normC)
            
            Red += (G[0] / 2) * normC
            Green += (G[1] / 2) * normC
            Blue += (G[2] / 2) * normC

        else:

            Red += (P[0] / 2) *  normC
            Green += (P[1] / 2) * normC
            Blue += (P[2] / 2) * normC
            
            Red += (G[0] / 2) * (2-normC)
            Green += (G[1] / 2) * (2-normC)
            Blue += (G[2] / 2) * (2-normC)   

        return pygame.Color(int(Red), int(Green), int(Blue))


# Display

SCREEN_NAME = "Particle Simulation"
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 585

FRAME_RATE = 30
CLICK_DELAY = 5

# Universal Constants

ZOOM = 3

class Universe:

    DECEL = 0.9

    REPULSION = 2
    BETA = 60
    AETHYR = 10
    ALPHA = 8
    GREAT_ATTRACTOR = 0.3