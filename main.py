import sys
import controller
from game_objects import *
import pygame.locals

pygame.init()

WIDTH = 1250
HEIGHT = 500
MAINSURF = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Hello World!')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

ctrl = controller.Controller()
sta1 = Station((50,50), MAINSURF)
ctrl.entities.append(sta1)

sta2 = Station((250,250), MAINSURF)
ctrl.entities.append(sta2)

trk1 = Track(sta1, sta2, [(250, 50), (150,150)], MAINSURF)
ctrl.entities.append(trk1)

trn1 = Train(sta1, "my_route", MAINSURF)
ctrl.entities.append(trn1)
while True:  # main game loop
    MAINSURF.fill(WHITE)
    
    ctrl.tick()
    
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()




