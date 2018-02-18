import pygame
from game_objects import *
from const import *

class Controller():
    entities = []
    
    fpsClock = pygame.time.Clock()
    
    def __init__(self):
        pass
    
    @staticmethod
    def tick():
        for entity in Controller.entities:
            entity.tick()
            entity.draw()
        
        pygame.display.update()
        Controller.fpsClock.tick(FPS)
    
    def save_map(self):
        print("xD")
        