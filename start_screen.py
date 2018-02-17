import pygame
#pass path as parameter
def draw_start_screen(surface, windowWidth, windowHeight):
	startImage = pygame.image.load("train.jpg")
	startImage = pygame.transform.scale(startImage, (windowWidth,windowHeight))
	startRect = startImage.get_rect()
	inStartScreen = True
	while inStartScreen:

		surface.blit(startImage, startRect)
		pygame.display.flip()

		for event in pygame.event.get():
			print(event)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					inStartScreen = False

