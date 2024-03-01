import src.shared.constants as c
import src.math.vectors as v
import pygame
import math

class Particle():

    def __init__(self, charge, mass, position):

        self.charge = charge
        self.mass = mass
        self.position = position

        self.speed = v.Zero()

        self.force = v.Zero()

        self.col = c.Colours.FROM_CHARGE(charge)

    def run(self, parts):

        self.behaivour(parts)

        self.speed = v.add(self.speed,  v.mult(self.force, 1 / self.mass))

        self.position = v.add(self.position, self.speed)

        self.speed = v.mult(self.speed, c.Universe.DECEL)

    def decay(self):

        pass

    def explode(self):

        pass

    def behaivour(self, parts):

        for i in parts:

            if i != self:
                        
                distance = v.sub(self.position, i.position)

                attrMag = c.Universe.GREAT_ATTRACTOR * i.mass/(distance.distance()**2)

                self.force = v.add(self.force, v.FromBearing(distance.angle(), attrMag))

                if distance.distance() < c.Universe.BETA:

                    magnitude = c.Universe.REPULSION * (math.sqrt(distance.distance() * i.mass) - math.sqrt(c.Universe.BETA));

                    self.force = v.add(self.force, v.FromBearing(distance.angle(), -magnitude))

                elif distance.distance() < c.Universe.BETA * 3:

                    potentialDiff = self.charge - i.charge

                    magnitude = math.sqrt((((1/distance.distance()) * potentialDiff) * c.Universe.ALPHA) ** 2) 

                    self.force = v.add(self.force, v.FromBearing(distance.angle(), magnitude))

        self.force = v.mult(self.force, 1 / (c.Universe.AETHYR * self.mass))

    def render(self, display, cameralocation):

        pygame.draw.circle(display, self.col, v.add(self.position, cameralocation).value(), self.mass * c.ZOOM)