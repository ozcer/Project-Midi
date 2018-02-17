import pygame
from const import *


class GameObject:
    pass


class Track(GameObject):
    
    def __init__(self, start_station, end_station, breakpoints: [(int, int)], surface):
        self.breakpoints = breakpoints
        self.start = start_station
        self.end = end_station
        self.color = BLACK
        self.surface = surface
    
    def tick(self):
        pass
    
    def draw(self):
        # connect as following
        # start_station - breakpoint1 - breakpoint2 ...-beakpointN - end_station
        point_list = list(self.breakpoints)
        point_list.insert(0, (self.start.x, self.start.y))
        point_list.append((self.end.x, self.end.y))
        pygame.draw.lines(self.surface, self.color, False, point_list)


class Station(GameObject):
    
    def __init__(self, pos: (int, int), surface):
        self.tracks = {} # "routeName": Track
        self.x = pos[0]
        self.y = pos[1]
        self.stationSize = 20
        self.surface = surface
    
    def addTrack(self, track):
        self.tracks.append(track)
    
    def send(self, train, track):
        pass
    
    def draw(self):
        pygame.draw.rect(self.surface, (0, 0, 255), [self.x - (self.stationSize/2), self.y-(self.stationSize/2), self.stationSize, self.stationSize])

    
    def tick(self):
        pass
    

class Train(GameObject):
    
    def __init__(self, parked_station, route, surface):
        self.track = None
        self.speed = 5
        self.x, self.y = parked_station.x, parked_station.y
        self.dimensions = (30, 10)
        self.surface = surface
        self.color = GREEN

    def travel_track(self, track):

        for bp in track:
            pass
    
    def draw(self):
        center_sprite = pygame.Rect(self.x - (self.dimensions[0]/2), self.y-(self.dimensions[1]/2), *self.dimensions)
        pygame.draw.rect(self.surface, self.color, center_sprite)
        
    def tick(self):
        pass