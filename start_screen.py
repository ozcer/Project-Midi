import pygame
import const
import sys
from pygame.locals import *

# pass path as parameter
def draw_start_screen(surface, windowWidth, windowHeight):
    startImage = pygame.image.load("train.png")
    #startImage = pygame.transform.scale(startImage, (windowWidth, windowHeight))
    startRect = startImage.get_rect(center=(const.DISPLAY_CENTER_X, const.DISPLAY_CENTER_Y))
    inStartScreen = True
    while True:

        surface.blit(startImage, startRect)

        font = pygame.font.Font("fonty.ttf", 45)
        small_font = pygame.font.Font("fonty.ttf", 25)
        title_text = font.render("Train Simulator:", True, const.RED)
        options_text = small_font.render("PRESS 1 FOR TOKYO, PRESS 2 FOR LONDON", True, const.RED)
        surface.blit(title_text, (50,50))
        surface.blit(options_text, (150, 150))
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
                    return "tokyo"
                if event.key == pygame.K_2:
                    return "london"

def background(image, resolution):
    pass

