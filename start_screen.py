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
    while inStartScreen:

        surface.blit(startImage, startRect)

        font = pygame.font.Font("fonty.ttf", 45)
        small_font = pygame.font.Font("fonty.ttf", 25)
        title_text = font.render("Train Simulator:", True, const.RED)
        options_text = small_font.render("PRESS 1 FOR TOKYO, PRESS 2 FOR VANCOUVER", True, const.RED)
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
                    inStartScreen = False
                if event.key == pygame.K_2:
                    inStartScreen = False


def message_to_screen(surface, msg, color, y_disp=0):
    font = pygame.font.SysFont(None, 25)
    screen_text = font.render(msg, True, color)
    surface.blit(screen_text, [(const.DISPLAY_WIDTH / 2), (const.DISPLAY_HEIGHT / 2)])

def background(image, resolution):
    pass

