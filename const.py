import pygame
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
GRAY = (153, 153, 153)
VIOLET = (138, 43, 226)
PINK = (255, 192, 203)

#UI
MAINSURF = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
DISPLAY_WIDTH, DISPLAY_HEIGHT = MAINSURF.get_size()
FPS = 144