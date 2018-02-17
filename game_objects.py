import pygame

class GameObject:
    pass

class Track(GameObject):

    def __init__(self, start_station, end_station, breakpoints: [(int, int)]):
        self.breakpoints = breakpoints
        self.start = start_station
        self.end = end_station
        self.color = (0,0,0)
        
    def draw(self):
        global MAINSURF
        # connect as following
        # start_station - breakpoint1 - breakpoint2 ...-beakpointN - end_station
        point_list = list(self.breakpoints)
        point_list.insert(0, (self.start_station.x, self.start_station.y))
        point_list.append((self.end_station.x, self.end_station.y))
        pygame.draw.lines(MAINSURF, self.color, False, point_list)

class Station:
    
    def __init__(self, pos: (int, int)):
        self.tracks = []
        self.x = pos[0]
        self.y = pos[1]
        self.stationSize = 10
        print("created station obj")
    
    def addTrack(self, track):
        self.tracks.append(track)
    
    def drawStation(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), [self.x, self.y, self.stationSize, self.stationSize])
