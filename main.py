import sys
import controller
import const
import start_screen
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
gamestate = "START"

ctrl = controller.Controller()
station1 = Station((50, 50), MAINSURF)
ctrl.entities.append(station1)

station2 = Station((250, 250), MAINSURF)
ctrl.entities.append(station2)

station3 = Station((50, 250), MAINSURF)
ctrl.entities.append(station3)

track1 = Track(station1, station2, [(250, 50), (200, 150)], MAINSURF)
ctrl.entities.append(track1)
station1.addTrack(track1, "route1")

track2 = Track(station2, station3, [(100, 150)], MAINSURF)
ctrl.entities.append(track2)
station2.addTrack(track2, "route1")

track3 = Track(station3, station1, [], MAINSURF)
ctrl.entities.append(track3)
station3.addTrack(track3, "route1")

train1 = Train(station1, "route1", MAINSURF)
station1.receive(train1)
ctrl.entities.append(train1)


start_screen.draw_start_screen(MAINSURF, const.DISPLAY_WIDTH, const.DISPLAY_HEIGHT)
while True:  # main game loop


    MAINSURF.fill(WHITE)
    
    ctrl.tick()
    
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()




