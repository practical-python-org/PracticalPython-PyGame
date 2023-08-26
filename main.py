import pygame as pg
import pygame_gui as gui
from home import HomeScreen
from game import Game
from settings import Settings
from other import Other
from common import COLORS, HEIGHT, WIDTH, FPS
from pygame_gui.core.interfaces.manager_interface import IUIManagerInterface


class Run:
    def __init__(self):
        pg.init()
        self.game_state = HomeScreen
        self.clock = pg.time.Clock()
        self.screen_size = (WIDTH, HEIGHT)
        self.btn_names = ['START', 'SETTINGS', 'OTHER']
        self.btn_class = [Game, Settings, Other]
        self.buttons = list()
        self.init_ui()
        self.events = self.get_events()
        self.game_loop()

    def init_ui(self):
        self.window_surface = pg.display.set_mode(self.screen_size)
        self.background = pg.Surface(self.screen_size)
        self.background.fill(COLORS["black"])
        self.manager = gui.UIManager(self.screen_size)

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

    def event_handler(self, running):
        for event in self.events["events"]:
            if event.type == pg.QUIT:
                return not running
            if (event.type == gui.UI_BUTTON_PRESSED
                    and self.buttons):
                for btn in self.buttons:
                    if event.ui_element == btn:
                        self.game_state = self.btn_dict[btn]
            self.manager.process_events(event)

    def game_loop(self):
        is_running = True
        while is_running:
            self.clock.tick(FPS)
            time_delta = self.events["dt"]
            self.events = self.get_events()
            tmp = self.event_handler(is_running)
            # return: bool if event == self.pg.QUIT
            if tmp is not None:
                is_running = tmp
            if self.game_state == HomeScreen:
                HomeScreen(self)
            else:  # state changed on button press
                run = self.game_state
                run(self)
            self.manager.update(time_delta)
            self.window_surface.blit(self.background, (0, 0))
            self.manager.draw_ui(self.window_surface)
            pg.display.update()


Run()
pg.quit()
