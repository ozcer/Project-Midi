import sys
import controller 
import GameObjects
import pygame.locals

pygame.init()

WIDTH = 350
HEIGHT = 400
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Hello World!')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

ctrl = controller.Controller()

station1 = GameObjects.Station([100, 100])

while True:  # main game loop
    DISPLAYSURF.fill(WHITE)
    station1.drawStation(DISPLAYSURF)
    
    ctrl.tick()
    
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()




