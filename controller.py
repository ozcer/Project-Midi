import pygame
from game_objects import *
from const import *

from pygame.locals import *


class Controller():
    entities = []
    
    fpsClock = pygame.time.Clock()
    
    def __init__(self, surf):
        self.surface = surf
        self.currentMoney = 0
        self.incomeRate = 100

    def tick(self):
        for entity in Controller.entities:
            entity.tick(self)
            entity.draw()

        money_font = pygame.font.SysFont(None, 25)
        text_surf =  money_font.render("Money: $" + str(self.currentMoney), True, (BLACK))
        self.surface.blit(text_surf, (25, DISPLAY_HEIGHT-25))
        
        rounded_fps = round(Controller.fpsClock.get_fps())
        text_surf = money_font.render("FPS: " + str(rounded_fps), True, (BLACK))
        self.surface.blit(text_surf, (10, 10))

        pygame.display.update()
        Controller.fpsClock.tick(FPS)

    def addMoney(self):
        self.currentMoney += self.incomeRate
