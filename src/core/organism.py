import src.shared.constants as c
import src.math.vectors as v
import src.core.particle as part
import random
import copy

class Ogranism:

    def __init__(self, position):

        self.position = position

        self.particles = []
        self.internalInteractions = []
        self.externalInteractions = []
        self.particleConfig = []

        self.MaxEnergy = c.MAX_ENERGY
        self.Energy = c.MAX_ENERGY / 2

        self.made = False

    def generate(self):

        # Interaction Table

        self.internalInteractions = []

        for i in range(0, c.particleTeams.TEAM_COUNT+1):

            self.internalInteractions.append([])

            for j in range(0, c.particleTeams.TEAM_COUNT+1):

                self.internalInteractions[i].append([

                    random.uniform(-1, 1), # Force
                    random.randrange(10, 15), # Repulsion Range
                    random.randrange(15, 70) # Attraction Range
                    
                ])

        # External Interactions
                
        self.externalInteractions = []

        for i in range(0, 3):

            self.externalInteractions.append([])

            for j in range(0, 3):

                self.externalInteractions[i].append(random.uniform(-1, 1))

        # Particle spawns

        self.particleConfig = []

        for i in range(0, c.LIFE_SIZE):

            self.particleConfig.append([

                v.Vector(random.randrange(-c.LIFE_SPREAD, c.LIFE_SPREAD), random.randrange(-c.LIFE_SPREAD, c.LIFE_SPREAD)), # Position
                random.randint(0, c.particleTeams.TEAM_COUNT) # Team

            ])

    def mutate(self):

        pass

    def create(self):

        self.particles = []

        for i in self.particleConfig:

            self.particles.append(part.Particle(i[1], v.add(self.position, i[0])))   

    def run(self, organisms, screenSize, food):

        self.Energy -= 1

        if (self.Energy < 0):

            organisms.remove(self)

        # Internal Forces

        for i in self.particles:

            for j in self.particles:

                if i == j:
                    continue

                if i.team == c.particleTeams.YELLOW:

                    for z in food:

                        distance = v.sub(i.position,z.position)

                        if distance.distance() < 10:

                            food.remove(z)

                            self.Energy += c.MAX_ENERGY / 10

                            if self.Energy >= self.MaxEnergy:
                                
                                self.Energy = self.MaxEnergy / 2
                                organisms.append(copy.deepcopy(self))

                                organisms[-1].position = v.add(organisms[-1].position, v.Vector(random.randrange(0, 100), random.randrange(0, 100)))
                                organisms[-1].mutate()
                                organisms[-1].create()

                dist = v.sub(i.position,j.position)

                dist = self.wrapDistance(dist, screenSize)

                mag = dist.distance()

                minDist = self.internalInteractions[i.team][j.team][1]
                radii = self.internalInteractions[i.team][j.team][2]

                #mag /= c.BETA

                if (mag > 0):
                    
                    if (mag < minDist):

                        force = dist.normalize()

                        force = v.mult(force, self.internalInteractions[i.team][j.team][0] * -3)
                        force = v.mult(force, mag / minDist)
                        force = v.mult(force, c.REPULSION)
                        i.force = v.add(i.force, force)

                    if (mag < radii):

                        force = dist.normalize()

                        force = v.mult(force, self.internalInteractions[i.team][j.team][0])
                        force = v.mult(force, mag / radii)
                        force = v.mult(force, c.ATTRACTION)

                        i.force = v.add(i.force, force)

                    i.force = v.add(i.force, v.FromBearing(dist.angle(), c.COHESION))

            i.run()

    def render(self, display, screenSize):

        for i in range(0, len(self.particles)):

            self.particles[i].render(display, screenSize)

    def wrapDistance(self, dist, screenSize):

        newDist = v.Vector(dist.x, dist.y)

        if (dist.x > 0.5 * screenSize[0]):

            newDist.x -= screenSize[0]

        if (dist.x < -0.5 * screenSize[0]):

            newDist.x += screenSize[0]

        if (dist.y > 0.5 * screenSize[1]):

            newDist.y -= screenSize[1]

        if (dist.y < -0.5 * screenSize[1]):

            newDist.y += screenSize[1]

        return newDist
    