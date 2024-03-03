import src.shared.constants as c
import src.math.vectors as v
import pygame


class Particle():

    def __init__(self, team, position):

        self.position = position

        self.mass = c.ZOOM

        self.col = c.FetchColFromTeam(team)

        self.team = team

        self.velocity = v.Zero()
        self.force = v.Zero()

    def run(self):

        self.velocity = v.add(self.velocity, v.mult(self.force, 1))

        self.position = v.add(self.position, v.mult(self.velocity, c.ZOOM))

        self.velocity = v.mult(self.velocity, 0.5)

        self.force = v.Zero()

    def render(self, display, screenSize):

        self.wrapPos(screenSize)

        pygame.draw.circle(display, self.col, self.position.value(), c.ZOOM)

    def wrapPos(self, screenSize):

        self.position.x = (self.position.x + screenSize[0]) % screenSize[0]
        self.position.y = (self.position.y + screenSize[1]) % screenSize[1]

        '''

        # Wrap X

        if self.position.x > screenSize[0]:

            self.position.x -= screenSize[0] + 10

        elif self.position.x < 0:

            self.position.x += screenSize[0] + 10

        # Wrap Y

        if self.position.y > screenSize[1]:

            self.position.y -= screenSize[1] + 10

        elif self.position.y < 0:

            self.position.y += screenSize[1] + 10

        '''