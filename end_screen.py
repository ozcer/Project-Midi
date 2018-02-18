import pygame
import sys
import const
from pygame.locals import *
from const import *

def draw_end_screen(surface, ):
    endImage = pygame.image.load("death.png")
    endRect = endImage.get_rect(center=(DISPLAY_CENTER_X, DISPLAY_CENTER_Y))
    while True:
        surface.fill(WHITE)
        surface.blit(endImage, endRect)

        font = pygame.font.Font("fonty.ttf", 45)
        small_font = pygame.font.Font("fonty.ttf", 25)
        title_text = font.render("YOU'VE GONE BANKRUPT!", True, RED)
        options_text = small_font.render("Unfortunately you have died of Light Wallet Disease", True, RED)
        surface.blit(title_text, (50, 50))
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