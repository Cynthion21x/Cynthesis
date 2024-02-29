import src.shared.constants as c
import src.math.vectors as v
import pygame

class Particle():

    def __init__(self, charge, mass, position):

        self.charge = charge
        self.mass = mass
        self.position = position

        self.speed = v.Zero()

        self.force = v.Zero()

        self.col = c.Colours.FROM_CHARGE(charge)

    def run(self):

        self.speed = v.add(self.speed,  v.mult(self.force, 1 / self.mass))

        self.position = v.add(self.position, self.speed)

        self.speed = v.sub(self.speed, v.mult(self.speed, c.Universe.DECEL))


    def render(self, display, cameralocation):

        pygame.draw.circle(display, self.col, v.add(self.position, cameralocation).value(), self.mass * c.ZOOM)