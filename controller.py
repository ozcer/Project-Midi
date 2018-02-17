import pygame


class Controller():
    entities = []
    
    FPS = 60
    fpsClock = pygame.time.Clock()
    
    def __init__(self):
        pass
    
    @staticmethod
    def tick():
        for entity in Controller.entities:
            entity.tick()
            entity.draw()
        
        pygame.display.update()
        Controller.fpsClock.tick(Controller.FPS)
