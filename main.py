import sys
import controller
from const import *
import start_screen
from game_objects import *
from pygame.locals import *
import map_editor

pygame.init()

editorMode = True

MAINSURF = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

pygame.display.set_caption('Hello World!')



ctrl = controller.Controller()
station1 = Station((50, 50), MAINSURF)
ctrl.entities.append(station1)

station2 = Station((600, 250), MAINSURF)
ctrl.entities.append(station2)

station3 = Station((50, 250), MAINSURF)
ctrl.entities.append(station3)

track1 = Track(station1, station2, [(700, 50)], MAINSURF)
ctrl.entities.append(track1)
station1.addTrack(track1, "route1")

track2 = Track(station2, station3, [(100, 150)], MAINSURF)
ctrl.entities.append(track2)
station2.addTrack(track2, "route1")

track3 = Track(station3, station1, [], MAINSURF)
ctrl.entities.append(track3)
station3.addTrack(track3, "route1")
station3.addTrack(track3, "short")

track5 = Track(station1, station3, [], MAINSURF)
ctrl.entities.append(track5)
station1.addTrack(track5, "short")

train1 = Train(station1, "route1", MAINSURF)
station1.receive(train1)
ctrl.entities.append(train1)

train2 = Train(station3, "short", MAINSURF)
station3.receive(train2)

ctrl.entities.append(train2)

start_screen.draw_start_screen(MAINSURF, DISPLAY_WIDTH, DISPLAY_HEIGHT)

while True:  # main game loop


    MAINSURF.fill(WHITE)
    
    ctrl.tick()

    keys = pygame.key.get_pressed()
    if keys[K_s]:
        ctrl.save_map()
        
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
        if editorMode == True:
        	if event.type == pygame.MOUSEBUTTONDOWN:
        		print(pygame.mouse.get_pos())
        		mousePos = pygame.mouse.get_pos()

        		newStation = Station(mousePos, MAINSURF)
        		ctrl.entities.append(newStation)



