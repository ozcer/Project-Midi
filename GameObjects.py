import pygame.locals


class Train:
    pass



class Track:
    pass



class Station:

	BLUE = (0, 0, 255)

	def __init__(self, pos: (int, int)):
		self.tracks = []
		self.x = pos[0]
		self.y = pos[1]
		self.stationSize = 10
		print("created station obj")

	def addTrack(self, track):
		self.tracks.append(track)

	def drawStation(self, surface): 
		pygame.draw.rect(surface, (0,0,255), [self.x, self.y, self.stationSize, self.stationSize])


