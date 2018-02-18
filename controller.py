import pygame
from game_objects import *
from const import *
from random import randint
from pygame.locals import *
from const import *


class Controller():
    entities = []
    
    fpsClock = pygame.time.Clock()


    
    def __init__(self, surf):
        self.surface = surf
        self.currentMoney = INITIAL_AMOUNT
        self.deductRate = 1000
        self.timeUntilDeduct = 1000
        self.deductPeriod = 1800
        self.positive = None


    def tick(self):
        self.handleExpense()
        for entity in Controller.entities:
            entity.tick(self)
            entity.draw()

        money_font = pygame.font.SysFont(None, 80)
        pos_surf = money_font.render("$"+str(self.currentMoney), True, (GREEN))
        neg_surf = money_font.render("$"+str(self.currentMoney), True, (RED))
        if self.currentMoney >= 0:
            self.surface.blit(pos_surf, (10, DISPLAY_HEIGHT-60))
        else:
            self.surface.blit(neg_surf, (10, DISPLAY_HEIGHT-60))
        
        rounded_fps = round(Controller.fpsClock.get_fps())
        text_surf = money_font.render("Wind: " + str(rounded_fps)+"km/hr", True, (BLACK))
        self.surface.blit(text_surf, (10, 10))

        #Legend ui
        legend_font = pygame.font.SysFont(None, 25)
        all_routes = set()
        for entity in Controller.entities:
            if type(entity) == Station:
                for route in entity.tracks:
                    all_routes.add(route)

        #randomized cloud generation
        if randint(0, 200) == 0:
            cloud1 = Cloud(self.surface)
            Controller.entities.append(cloud1)


        pygame.display.update()
        Controller.fpsClock.tick(FPS)

    def addMoney(self, delta):
        self.currentMoney += delta

    def handleExpense(self):
        if self.timeUntilDeduct is 0:
            self.currentMoney -= self.deductRate
            self.timeUntilDeduct = self.deductPeriod
        else:
            self.timeUntilDeduct -= 1

    def get_money(self):
        return self.currentMoney

