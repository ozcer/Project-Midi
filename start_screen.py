import pygame
import const
import sys
from pygame.locals import *

# pass path as parameter
def draw_start_screen(surface, windowWidth, windowHeight):
    startImage = pygame.image.load("train.jpg")
    startImage = pygame.transform.scale(startImage, (windowWidth, windowHeight))
    startRect = startImage.get_rect()
    inStartScreen = True
    while inStartScreen:

        surface.blit(startImage, startRect)
        font = pygame.font.Font("fonty.ttf", 45)
        font = font.render("PRESS 1 OR 2 TO BEGIN", True, const.RED)
        surface.blit(font, (50,50))
        pygame.display.update()

        keys = pygame.key.get_pressed()

        if keys[K_ESCAPE]:
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    inStartScreen = False
                if event.key == pygame.K_2:
                    inStartScreen = False


def message_to_screen(surface, msg, color, y_disp=0):
    font = pygame.font.SysFont(None, 25)
    screen_text = font.render(msg, True, color)
    surface.blit(screen_text, [(const.DISPLAY_WIDTH / 2), (const.DISPLAY_HEIGHT / 2)])

def background(image, resolution):
    pass

