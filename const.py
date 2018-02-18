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
POP_RATE = 2
TRAIN_CAPACITY = 20
INCOME_RATE = 20

#Balancing variables
TRAIN_COST = 1000
BANKRUPT_AMOUNT = -500
INITIAL_AMOUNT = 10000
COST_OF_MOUNTAIN = 4000



#Pictures
HAPPY = pygame.image.load("happy.png")
NEUTRAL = pygame.image.load("neutural.png")
ANGRY = pygame.image.load("sad.png")
HAPPYIMG = pygame.transform.scale(HAPPY, (25, 25))
NEUTRALIMG = pygame.transform.scale(NEUTRAL, (25, 25))
ANGRYIMG = pygame.transform.scale(ANGRY, (25, 25))

CLOUD = pygame.image.load("cloud.png")