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

        self.window = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT), pygame.RESIZABLE)

        self.clock = pygame.time.Clock()

        # Time Control

        self.deltaTime = 0

        # World

        self.particles = []
        self.particleCount = particleC


    def coreLoop(self):

        self.reset()

        cp = v.Zero()
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
                cVel.y -= 300 * self.deltaTime
                
            if keys[pygame.K_s]:
                cVel.y += 300 * self.deltaTime
                    
            if keys[pygame.K_a]:
                cVel.x -= 300 * self.deltaTime

            if keys[pygame.K_d]:

                cVel.x += 300 * self.deltaTime

            cp = v.add(cp, cVel)
            cVel = v.mult(cVel, c.Universe.DECEL)
             
            # Process World
                    
            for i in self.particles:

                i.run()
                i.render(self.display, cp)

            # Update Display

            self.window.blit(self.display, (0, 0))
            pygame.display.flip()

            self.deltaTime = self.clock.tick(c.FRAME_RATE) / 1000

            # Exit at end

            if quitting:
                self.close()

    def reset(self):

        self.particles = []

        for i in range(0, self.particleCount):

            charge = random.uniform(-1, 1)
            mass = 1 + random.uniform(0, 1)

            particle = part.Particle(charge, mass, v.Zero())

            self.particles.append(particle)
            
    def close(self):

        pygame.quit()
        self.running = False