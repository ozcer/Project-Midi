import pygame
from game_objects import *
from const import *

from pygame.locals import *
from const import *


class Controller():
    entities = []
    
    fpsClock = pygame.time.Clock()
    
    def __init__(self, surf):
        self.surface = surf
        self.currentMoney = 0
        self.incomeRate = 25

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

        #Legend ui
        legend_font = pygame.font.SysFont(None, 25)
        all_routes = set()
        for entity in Controller.entities:
            if type(entity) == Station:
                for route in entity.tracks:
                    all_routes.add(route)

        legend_text = legend_font.render(f"Train route: {all_routes}", True, BLACK)
        self.surface.blit(legend_text, (DISPLAY_WIDTH-300, DISPLAY_HEIGHT-150))

        pygame.display.update()
        Controller.fpsClock.tick(FPS)

    def addMoney(self, passCount):
        self.currentMoney += self.incomeRate * passCount
