import game_objects

class Track(game_objects.GameObject):
    
    def __init__(self, start_station, end_station, breakpoints: [(int, int)]):
        self.breakpoints = breakpoints
        self.start = start_station
        self.end = end_station
        self.color = (0, 0, 0)
    
    def draw(self):
        global MAINSURF
        # connect as following
        # start_station - breakpoint1 - breakpoint2 ...-beakpointN - end_station
        point_list = list(self.breakpoints)
        point_list.insert(0, (self.start_station.x, self.start_station.y))
        point_list.append((self.end_station.x, self.end_station.y))
        pygame.draw.lines(MAINSURF, self.color, False, point_list)
