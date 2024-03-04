import pygame
import os

# Assets Path

ASSETS_PATH = os.path.join(os.path.dirname(__file__), '..', '..', "assets")

# Program Data

DATA_PATH = os.path.join(os.getenv('APPDATA'), '..', 'LocalLow', 'Cynthion21x', 'Cynthesis')

# Colours

class Colours:

    RED = pygame.Color(204, 39, 61)
    BLUE = pygame.Color(38, 50, 181)
    GREEN = pygame.Color(49, 161, 91)
    PURPLE = pygame.Color(122, 9, 214)
    YELLOW = pygame.Color(252, 219, 3)

    WHITE = pygame.Color(255, 255, 255)
    BLACK = pygame.Color(0, 0 ,0)


# Display

SCREEN_NAME = "Cynthesis"
START_SCREEN_WIDTH = 1040
START_SCREEN_HEIGHT = 585

FRAME_RATE = 60
CLICK_DELAY = 5

# Universal Constants

ZOOM = 3
LIFE_SPREAD = 1000
LIFE_SIZE = 100
MAX_ENERGY = 5000

BETA = 10

REPULSION = 0.1
ATTRACTION = 0.1
DECEL = 0.85

COHESION = 0
FOOD_COUNT = 100

class particleTeams:

    FOOD = -1
    GREEN = 0
    BLUE = 1
    YELLOW = 2
    PURPLE = 3

    TEAM_COUNT = 3

def FetchColFromTeam(team):
    
    if team == 0:

        return Colours.GREEN
    
    if team == 1:

        return Colours.BLUE
    
    if team == 2:

        return Colours.YELLOW
    
    if team == 3:

        return Colours.PURPLE
    
    if team == -1:

        return Colours.RED
