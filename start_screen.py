import pygame
import sys
import end_screen
from pygame.locals import *
from const import *

# pass path as parameter
def draw_start_screen(surface):
    startImage = pygame.image.load("mountain.png")
    startRect = startImage.get_rect(center=(DISPLAY_CENTER_X, DISPLAY_CENTER_Y))
    while True:

        surface.fill(WHITE)
        surface.blit(startImage, startRect)

        font = pygame.font.Font("fonty.ttf", 45)
        small_font = pygame.font.Font("fonty.ttf", 25)
        title_text = font.render("Gondola Simulator:", True, BLACK)
        options_text = small_font.render("1: SNOWPEAK SUMMIT 2: MISTY MOUNTAIN 3: FREE-FORM FUN", True, BLACK)
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
                if event.key == pygame.K_3:
                    return "free"
