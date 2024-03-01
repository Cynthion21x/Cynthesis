import pygame
import src.shared.constants as c
import src.core.particle as part
import random
import src.math.vectors as v

class simulation:

    def __init__(self, particleC):

        pygame.init()

        self.running = True

        # Display

        self.display = pygame.Surface((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

        self.window = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

        pygame.display.set_caption(c.SCREEN_NAME)

        self.clock = pygame.time.Clock()

        # Time Control

        self.deltaTime = 0

        # World

        self.particles = []
        self.particleCount = particleC

        self.cp = v.Zero()


    def coreLoop(self):

        self.reset()
        cVel = v.Zero()

        while self.running:

            # Clear Screen

            quitting = False
            self.display.fill(c.Colours.BLACK)

            # Events

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitting = True

            # Camera Controls
            
            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                cVel.y += 300 * self.deltaTime
                
            if keys[pygame.K_s]:
                cVel.y -= 300 * self.deltaTime
                    
            if keys[pygame.K_a]:
                cVel.x += 300 * self.deltaTime

            if keys[pygame.K_d]:

                cVel.x -= 300 * self.deltaTime

            self.cp = v.add(self.cp, cVel)
            cVel = v.mult(cVel, 0.3)
             
            # Process World
                    
            for i in self.particles:

                i.run(self.particles)
                i.render(self.display, self.cp)

            # Update Display

            self.window.blit(self.display, (0, 0))
            pygame.display.flip()

            self.deltaTime = self.clock.tick(c.FRAME_RATE) / 1000

            # Exit at end

            if quitting:
                self.close()

    def reset(self):

        self.cp = v.Vector(c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2)

        self.particles = []

        for i in range(0, self.particleCount):

            charge = random.uniform(-1, 1)
            mass = 1 + random.uniform(0, 1)

            particle = part.Particle(charge, mass, v.Vector(random.uniform(-3, 3), random.uniform(-3, 3)))

            self.particles.append(particle)
            
    def close(self):

        pygame.quit()
        self.running = False