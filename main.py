import sys
import controller
from const import *
import start_screen
from game_objects import *
from pygame.locals import *

pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(64)
pygame.mixer.music.load("zelda.mp3")
pygame.mixer.music.play()
choo_sound = pygame.mixer.Sound("choo.wav")

MAINSURF = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
DISPLAY_WIDTH, DISPLAY_HEIGHT = MAINSURF.get_size()
bg = pygame.image.load("tokyo.png")
bg = pygame.transform.scale(bg, (DISPLAY_WIDTH, DISPLAY_HEIGHT))


pygame.display.set_caption('SkyTrain Sim')

ctrl = controller.Controller(MAINSURF)
station1 = Station((50, 50), MAINSURF)
ctrl.entities.append(station1)

station2 = Station((1200, 250), MAINSURF)
ctrl.entities.append(station2)

station3 = Station((50, 400), MAINSURF)
ctrl.entities.append(station3)

track1 = Track(station1, station2, [(1000, 50)], MAINSURF)
ctrl.entities.append(track1)
station1.addTrack(track1, "route1")

track2 = Track(station2, station3, [(500, 200)], MAINSURF)
ctrl.entities.append(track2)
station2.addTrack(track2, "route1")

track3 = Track(station3, station1, [], MAINSURF)
ctrl.entities.append(track3)
station3.addTrack(track3, "route1")
station3.addTrack(track3, "short")

track5 = Track(station1, station3, [], MAINSURF)
ctrl.entities.append(track5)
station1.addTrack(track5, "short")

train1 = Train(station1, "route1", MAINSURF)
station1.receive(train1, ctrl)
ctrl.entities.append(train1)

train2 = Train(station3, "short", MAINSURF)
station3.receive(train2, ctrl)

ctrl.entities.append(train2)

start_screen.draw_start_screen(MAINSURF, DISPLAY_WIDTH, DISPLAY_HEIGHT)

selected_stations = []


def create_station(pos, surface):
    new_station = Station(pos, surface)
    ctrl.entities.append(new_station)
    choo_sound.play()


def create_track(start, end, breakpoints, surface=MAINSURF):
    new_track = Track(start, end, [], surface)
    ctrl.entities.append(new_track)


def clear_selected_stations(select_list):
    for station in select_list:
        station.color = BLUE
    del select_list[:]

while True:  # main game loop


    MAINSURF.blit(bg,(0, 0))
    
    ctrl.tick()

    keys = pygame.key.get_pressed()

    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
            
        # left click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                clicked_on_station = None
                for entity in controller.Controller.entities:
                    if type(entity) == Station and entity.sprite.collidepoint(mouse_pos):
                        print("clicking on station: ", entity.sprite)
                        clicked_on_station = entity
                        selected_stations.append(clicked_on_station)
                if not clicked_on_station:
                    create_station(mouse_pos, MAINSURF)
                else:
                    clicked_on_station.color = YELLOW
                    if len(selected_stations) == 2:
                        create_track(selected_stations[0], selected_stations[1], [])
                        clear_selected_stations(selected_stations)
            elif event.button == 2:
                print(selected_stations)
            elif event.button == 3:
                clear_selected_stations(selected_stations)