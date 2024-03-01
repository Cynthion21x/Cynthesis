import src.shared.constants as c
import src.math.vectors as v
import pygame
import math
import random

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

        if (self.speed.distance() < 0.06 and self.mass > 1):

            explodeChange = random.randint(0, 1000)

            if explodeChange > c.Universe.DECAY:

                self.explode(parts)

        if (self.mass < 1):

            parts.remove(self)
            del self

        decayChange = random.randint(0, 1000)

        if decayChange > c.Universe.DECAY:

            if (self.charge < 0):

                self.charge += (1 + self.charge) * 0.5

            else:

                self.charge -= (1 - self.charge) * 0.5

            self.mass /= 1.2

            self.col = c.Colours.FROM_CHARGE(self.charge)

    def decay(self):

        pass

    def explode(self, parts):

        randomForce = v.Vector(random.uniform(-2, 2), random.uniform(-2, 2))

        parts.append(Particle(-self.charge / 2, self.mass / 1.3, self.position))
        parts.append(Particle(self.charge / 2, self.mass / 1.3, v.add(self.position, v.Vector(random.uniform(0, 2), random.uniform(0, 2)))))

        parts[len(parts) - 1].speed = v.mult(randomForce, 6)
        parts[len(parts) - 2].speed = v.mult(randomForce, -6)

        parts.remove(self)
        del self

    def behaivour(self, parts):

        for i in parts:

            if i != self:
                        
                distance = v.sub(self.position, i.position)

                attrMag = c.Universe.GREAT_ATTRACTOR * i.mass/(distance.distance()**2)

                self.force = v.add(self.force, v.FromBearing(distance.angle(), attrMag))

                if distance.distance() < c.Universe.BETA + i.mass:

                    magnitude = i.mass * c.Universe.REPULSION * (math.sqrt(distance.distance()) - math.sqrt(c.Universe.BETA + i.mass));

                    self.force = v.add(self.force, v.FromBearing(distance.angle(), -magnitude))

                elif distance.distance() < c.Universe.BETA * 3:

                    potentialDiff = self.charge - i.charge

                    magnitude = math.sqrt((((1/distance.distance()) * potentialDiff) * c.Universe.ALPHA) ** 2) 

                    self.force = v.add(self.force, v.FromBearing(distance.angle(), magnitude))

        self.force = v.mult(self.force, 1 / (c.Universe.AETHYR * self.mass))

    def render(self, display, cameralocation):

        pygame.draw.circle(display, self.col, v.add(self.position, cameralocation).value(), self.mass * c.ZOOM)