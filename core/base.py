import pygame
import sys
from core.input import Input

class Base:
    def __init__(self):
        pygame.init()
        screenSize = (512, 512)
        displayFlags = pygame.DOUBLEBUF | pygame.OPENGL
        
        
        # antialiasing
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        
        # use core profile for cross-platform compatibility
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK,pygame.GL_CONTEXT_PROFILE_CORE)

        self.screen = pygame.display.set_mode(screenSize, displayFlags)
        pygame.display.set_caption("First Window")
        
        self.running = True
        self.clock = pygame.time.Clock()
        self.input = Input()
        self.fps = 60

    # abstract methods
    def initialize(self):
        pass
    def update(self):
        pass

    # application life cycle
    def run(self):
        # startup stage
        self.initialize()
        # main loop
        while self.running:
            # process input
            self.input.update()
            if self.input.quit:
                self.running = False
            self.update()
            #self.render()
            pygame.display.flip() # double buffer flip
            self.clock.tick(self.fps)
        
        pygame.quit()
        sys.exit()
        


