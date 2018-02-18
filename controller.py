import pygame
from game_objects import *
from const import *

class Controller():
    entities = []
    
    fpsClock = pygame.time.Clock()
    
    def __init__(self):
        self.currentMoney = 0
        self.incomeRate = 1

    def tick(self):
        for entity in Controller.entities:
            entity.tick(self)
            entity.draw()
        
        pygame.display.update()
        Controller.fpsClock.tick(FPS)

    def addMoney(self):
        self.currentMoney += self.incomeRate
