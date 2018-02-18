import pygame
import const
#pass path as parameter
def draw_start_screen(surface, windowWidth, windowHeight):
	startImage = pygame.image.load("train.jpg")
	startImage = pygame.transform.scale(startImage, (windowWidth,windowHeight))
	startRect = startImage.get_rect()
	inStartScreen = True
	while inStartScreen:

		surface.blit(startImage, startRect)
		pygame.display.update()

		message_to_screen(surface, "Press space to continue", const.BLACK)
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					inStartScreen = False



def message_to_screen(surface, msg, color, y_disp=0):
	font = pygame.font.SysFont(None, 25)
	screen_text = font.render(msg, True, color)
		# textRect.center = ((const.DISPLAY_WIDTH / 2), (const.DISPLAY_HEIGHT / 2)+ y_disp)
	surface.blit(screen_text, [(const.DISPLAY_WIDTH / 2), (const.DISPLAY_HEIGHT / 2)])

