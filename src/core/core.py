import pygame
import src.shared.constants as c
import src.core.organism as org
import random
import src.math.vectors as v
import src.core.particle as part

class simulation:

    def __init__(self, particleC):

        pygame.init()

        self.running = True

        # Display

        self.display = pygame.Surface((c.START_SCREEN_WIDTH, c.START_SCREEN_HEIGHT))

        self.window = pygame.display.set_mode((c.START_SCREEN_WIDTH, c.START_SCREEN_HEIGHT), pygame.RESIZABLE)

        pygame.display.set_caption(c.SCREEN_NAME)

        self.clock = pygame.time.Clock()

        # Time Control

        self.deltaTime = 0

        # World

        self.organisms = []
        self.particleCount = particleC

        self.food = []

    def coreLoop(self):

        self.reset()

        while self.running:

            # Clear Screen

            quitting = False
            self.display.fill(c.Colours.BLACK)

            self.screenSize = self.window.get_size()

            # Events

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitting = True

                if event.type == pygame.VIDEORESIZE:

                    self.display = pygame.Surface(event.size)

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:

                        self.reset()
             
            # Process World
                    
            if (len(self.food) < c.FOOD_COUNT):

                self.food.append(part.Particle(-1, v.Vector(random.randrange(0, self.screenSize[0]), random.randrange(0, self.screenSize[1]))))                    

            for i in self.food:

                i.render(self.display, self.screenSize)

            for i in self.organisms:

                i.run(self.organisms, self.screenSize, self.food)
                i.render(self.display, self.screenSize)

            # Update Display

            self.window.blit(self.display, (0, 0))
            
            pygame.display.flip()

            self.deltaTime = self.clock.tick(c.FRAME_RATE) / 1000

            # Exit at end

            if quitting:
                self.close()

    def reset(self):

        self.organisms = []

        for i in range(0, self.particleCount):

            organism = org.Ogranism(v.Vector(random.randrange(0, c.START_SCREEN_WIDTH), random.randrange(0, c.START_SCREEN_HEIGHT)))

            self.organisms.append(organism)

            self.organisms[i].generate()
            self.organisms[i].create()
            
    def close(self):

        pygame.quit()
        self.running = False