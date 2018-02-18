import pygame
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 170)
GREEN = (0, 148, 0)
YELLOW = (255, 224, 0)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
GRAY = (153, 153, 153)
VIOLET = (138, 43, 226)
PINK = (255, 192, 203)

#UI
MAINSURF = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
DISPLAY_WIDTH, DISPLAY_HEIGHT = MAINSURF.get_size()
DISPLAY_CENTER_X, DISPLAY_CENTER_Y = DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2
FPS = 60
POP_RATE = 1
TRAIN_CAPACITY = 10