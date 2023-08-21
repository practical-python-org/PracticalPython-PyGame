import pygame as pg
import pygame_gui

from common import COLORS, HEIGHT, WIDTH, FPS


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
                            print('Hello World!')

                self.manager.process_events(event)

            self.manager.update(time_delta)

            self.window_surface.blit(self.background, (0, 0))
            self.manager.draw_ui(self.window_surface)

            pg.display.update()


RunGame()
# Close pygame
pg.quit()