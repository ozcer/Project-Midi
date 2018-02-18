import pygame
from math import sin, cos, pi, atan2, hypot
from const import *


def dist(destination, origin):
    return hypot(destination[0] - origin[0], destination[1] - origin[1])


class GameObject:
    pass


class Track(GameObject):
    
    def __init__(self, start_station, end_station, breakpoints: [(int, int)], surface, color=BLACK):
        self.breakpoints = breakpoints
        self.start_station = start_station
        self.end_station = end_station
        self.surface = surface
        self.color = color
    
    def tick(self):
        pass

    def update_color(self, new_color):
        self.color = new_color
    
    def draw(self):
        # Connect as following
        # Start_station - breakpoint1 - breakpoint2 ...-beakpointN - end_station
        point_list = list(self.breakpoints)
        point_list.insert(0, (self.start_station.x, self.start_station.y))
        point_list.append((self.end_station.x, self.end_station.y))
        pygame.draw.lines(self.surface, self.color, False, point_list)


class Station(GameObject):
    
    def __init__(self, pos: (int, int), surface):
        self.tracks = {} # "routeName": Track
        self.x = pos[0]
        self.y = pos[1]
        self.stationDimensions = 20
        self.surface = surface
    
    def addTrack(self, track, route):
        self.tracks[route] = track
    
    def send(self, train, track):
        train.travel_track(track)
    
    def receive(self, train):
        target_track = self.tracks[train.route]
        self.send(train, target_track)
    
    def draw(self):
        pygame.draw.rect(self.surface, (0, 0, 255), [self.x - (self.stationSize/2), self.y-(self.stationSize/2), self.stationSize, self.stationSize])

    
    def tick(self):
        pass
    

class Train(GameObject):
    
    def __init__(self, parked_station, route, surface):
        self.destination = (0,0)
        self.route = route
        self.speed = 5
        self.route = route
        self.x, self.y = parked_station.x, parked_station.y
        self.dimensions = (30, 10)
        self.angle = 0
        self.sprite = pygame.Rect(self.x, self.y, *self.dimensions)
        self.surface = surface
        self.color = GREEN

    def travel_track(self, track):
        self.i = 0
        self.destination = (track.end_station.x, track.end_station.y) if len(track.breakpoints) == 0 else track.breakpoints[0]
        self.track = track
        
    
    def get_angle(self,destination):
        x_dist = destination[0] - self.x
        y_dist = destination[1] - self.y
        return atan2(-y_dist, x_dist) % (2 * pi)

    def project(self):
        return (round(self.x + (cos(self.angle) * self.speed)),
                round(self.y - (sin(self.angle) * self.speed)))
    
    def at(self, destination, within=3):
        return dist(destination, (self.x, self.y)) <= within
    
    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.sprite)
        
    def tick(self):
        self.angle = self.get_angle(self.destination)
        self.x, self.y = self.project()
        self.sprite.center = (self.x, self.y)
        # If it has reaches the destination
        if dist(self.destination, (self.x, self.y)) <= 3:
            self.i += 1
            # If it is not at end station
            if not self.at((self.track.end_station.x, self.track.end_station.y)):
                # If out of breakpoints, head to end station
                if self.i > len(self.track.breakpoints)-1:
                    self.destination = (self.track.end_station.x, self.track.end_station.y)
                else:
                    # Else head to next breakpoint
                    self.destination = self.track.breakpoints[self.i]
            else: # If at end station
                self.i = 0
                self.track.end_station.receive(self)