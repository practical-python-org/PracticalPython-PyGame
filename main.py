import pygame as pg
import pygame_gui

from common import COLORS, HEIGHT, WIDTH, FPS, TILE_SIZE, VERTICAL_TILE_NUM, HORIZONTAL_TILE_NUM
from components.map.mapmanager import MapManager
from components.characters.player import Player
from utilities.logger import log_info


class RunGame:
    def __init__(self):
        self.clock = pg.time.Clock()
        self.screen_size = (WIDTH, HEIGHT)
        self.buttons = list()
        self.init_ui()
        self.game_loop()


    def init_ui(self):
        pg.init()
        pg.display.set_caption('Quick Start')
        self.window_surface = pg.display.set_mode(self.screen_size)
        self.background = pg.Surface(self.screen_size)
        self.background.fill(COLORS["black"])

        self.manager = pygame_gui.UIManager(self.screen_size)

        self.set_buttons()


    def set_buttons(self):
        def offset_button(top_left):
            padding = 80
            top_left[1] += padding
            return top_left

        btn_width, btn_height = 100, 50
        top_left = [WIDTH//2 - btn_width//2, btn_height]
        dimensions = (btn_width, btn_height)

        self.button = pg.Rect(top_left, dimensions)
        self.btn_names = ['START', 'SETTINGS', 'OTHER']
        for btn_name in self.btn_names:
            btn = pygame_gui.elements.UIButton(relative_rect=self.button,
                                               text=btn_name,
                                               manager=self.manager)
            self.buttons.append(btn)
            self.button = pg.Rect(offset_button(top_left), dimensions)


    def get_events(self):
        """
        Returns necessary events for application. Packed in a dictionary.
        """
        events = pg.event.get()
        mouse_press = pg.mouse.get_pressed()
        keys = pg.key.get_pressed()
        mouse_pos = pg.mouse.get_pos()
        raw_dt = self.clock.get_time()
        dt = raw_dt * FPS

        return {
            "events": events,
            "mouse press": mouse_press,
            "keys": keys,
            "mouse pos": mouse_pos,
            "raw dt": raw_dt,
            "dt": dt,
        }

    
    def game_loop(self):

        is_running = True

        player_coords = (WIDTH // 2, HEIGHT // 2)
        player = Player(self.window_surface, player_coords[0], player_coords[1], 50, 50)

        map_manager = MapManager(self.window_surface, TILE_SIZE, VERTICAL_TILE_NUM, HORIZONTAL_TILE_NUM)
        map_manager.load_map()
        map_manager.enable_debug()

        while is_running:

            #time_delta = clock.tick(FPS) / 1000.0 

            self.clock.tick(FPS)

            events = self.get_events()

            time_delta = events["dt"]

            for event in events["events"]:
                if event.type == pg.QUIT:
                    is_running = False

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    for btn in self.buttons:
                        if event.ui_element == btn:
                            log_info(f'{btn.text} was pressed!')

                if event.type == pg.MOUSEBUTTONDOWN and map_manager.debug:
                    if event.button == 1:
                        log_info(f'Left mouse button was pressed at {events["mouse pos"]}')
                        # Create tile based on mouse position at nearest tile
                        closest_tile = (events["mouse pos"][0] // TILE_SIZE, events["mouse pos"][1] // TILE_SIZE)
                        log_info(f'Closest tile is {closest_tile}')
                        # selected_tiles.append(closest_tile)
                        map_manager.save_map(closest_tile)
                    if event.button == 3:
                        log_info(f'Right mouse button was pressed at {events["mouse pos"]}')
                        # Delete tile based on mouse position at nearest tile
                        closest_tile = (events["mouse pos"][0] // TILE_SIZE, events["mouse pos"][1] // TILE_SIZE)
                        log_info(f'Closest tile is {closest_tile}')
                        map_manager.delete_object(closest_tile)

                self.manager.process_events(event)

            self.manager.update(time_delta)

            self.window_surface.blit(self.background, (0, 0))
            self.manager.draw_ui(self.window_surface)

            player.update()

            # Draw UI
            self.manager.draw_ui(self.window_surface)
            
            if map_manager.debug:
                map_manager.draw_tile_grid()

                for tile in map_manager.load_map():
                    map_manager.render_object("tile", tile)
                    
            pg.display.update()


RunGame()
# Close pygame
pg.quit()