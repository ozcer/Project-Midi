import sys
import controller
from const import *
import start_screen
from game_objects import *
from pygame.locals import *

pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(64)
pygame.mixer.music.load("ambient.mp3")
pygame.mixer.music.play()

pygame.display.set_caption('TRAIN SIMULATOR')

MAINSURF = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
DISPLAY_WIDTH, DISPLAY_HEIGHT = MAINSURF.get_size()

#Our main menu function now returns our map choice, fyi
map_choice = start_screen.draw_start_screen(MAINSURF, DISPLAY_WIDTH, DISPLAY_HEIGHT)
bg = pygame.image.load(map_choice + ".png").convert()
bg = pygame.transform.scale(bg, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
ctrl = controller.Controller(MAINSURF)
if map_choice == "tokyo":
    station1 = Station((198, 162), MAINSURF, "Mount Keefer")
    ctrl.entities.append(station1)

    station2 = Station((920, 540), MAINSURF, "The Spire")
    ctrl.entities.append(station2)

    station3 = Station((161, 410), MAINSURF, "The Peaks")
    ctrl.entities.append(station3)

    track1 = Track(station1, station2, [(550, 250)], MAINSURF)
    ctrl.entities.append(track1)
    station1.addTrack(track1)

    track2 = Track(station2, station3, [(500, 500)], MAINSURF)
    ctrl.entities.append(track2)
    station2.addTrack(track2)

    track3 = Track(station3, station1, [], MAINSURF)
    ctrl.entities.append(track3)
    station3.addTrack(track3)
    station3.addTrack(track3)

    track5 = Track(station1, station3, [], MAINSURF)
    ctrl.entities.append(track5)
    station1.addTrack(track5)

    train1 = Train(station1, MAINSURF)
    station1.receive(train1, ctrl)
    ctrl.entities.append(train1)

    train2 = Train(station3, MAINSURF)
    station3.receive(train2, ctrl)

    ctrl.entities.append(train2)

    selected_stations = []

if map_choice == "london":
    station1 = Station((382, 363), MAINSURF, "Wery's Pass")
    ctrl.entities.append(station1)

    station2 = Station((783, 155), MAINSURF, "Johnny-Old Hill")
    ctrl.entities.append(station2)

    station3 = Station((1040, 572), MAINSURF, "Piddlty Wellington Summmit")
    ctrl.entities.append(station3)

    track1 = Track(station1, station2, [(420, 211)], MAINSURF)
    ctrl.entities.append(track1)
    station1.addTrack(track1)

    track2 = Track(station2, station3, [(911, 402)], MAINSURF)
    ctrl.entities.append(track2)
    station2.addTrack(track2)

    track3 = Track(station3, station1, [(660,623)], MAINSURF)
    ctrl.entities.append(track3)
    station3.addTrack(track3)
    station3.addTrack(track3)

    track5 = Track(station1, station3, [], MAINSURF)
    ctrl.entities.append(track5)
    station1.addTrack(track5)

    train1 = Train(station1, MAINSURF)
    station1.receive(train1, ctrl)
    ctrl.entities.append(train1)

    train2 = Train(station3, MAINSURF)
    station3.receive(train2, ctrl)

    ctrl.entities.append(train2)

    selected_stations = []

if map_choice == "free":
    selected_stations = []

tooltip = {"msg":"", "pos":(DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2), "time":200}
ttfont = pygame.font.SysFont(None, 20)
def draw_tooltip():
    if tooltip["time"] > 0:
        text_surf = ttfont.render(tooltip["msg"], True, RED)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_y -= 10
        MAINSURF.blit(text_surf, (mouse_x, mouse_y))
        tooltip["time"] -= 1


def create_station(pos, surface, ctrl):
    if ctrl.get_money() >= 300:
        new_station = Station(pos, surface)
        ctrl.entities.append(new_station)
        ctrl.addMoney(-300)
    else:
        tooltip["msg"] = "NOT ENOUGH MONEY!"
        tooltip["pos"] = mouse_pos
        tooltip["time"] = 50



def create_track(start, end, breakpoints, surface=MAINSURF):
    new_track = Track(start, end, [], surface)
    ctrl.entities.append(new_track)
    start.addTrack(new_track)

    new_track2 = Track(end, start, [], surface)
    ctrl.entities.append(new_track2)
    end.addTrack(new_track2)


def clear_selected_stations(select_list):
    for station in select_list:
        station.color = BLUE
    del select_list[:]

while True:  # main game loop
    
    #MAINSURF.fill(WHITE)
    MAINSURF.blit(bg,(0, 0))
    draw_tooltip()
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
                    r, g, b, a = MAINSURF.get_at(mouse_pos)
                    if b >= 230:
                        tooltip["msg"] = "CANNOT BUILD IN THE AIR!"
                        tooltip["pos"] = mouse_pos
                        tooltip["time"] = 100
                    else:
                        create_station(mouse_pos, MAINSURF, ctrl)
                else:
                    clicked_on_station.color = YELLOW
                    if len(selected_stations) == 2:
                        create_track(selected_stations[0], selected_stations[1], [])
                        clear_selected_stations(selected_stations)
            elif event.button == 2:
                print(selected_stations)
            elif event.button == 3:
                clear_selected_stations(selected_stations)