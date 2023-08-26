import pygame as pg
import pygame_gui as gui
from common import COLORS, HEIGHT, WIDTH, FPS
from game import Game
from settings import Settings
from other import Other


class HomeScreen:

    def __init__(self, run):
        self.run = run
        self.home_screen()

    def home_screen(self):
        self.set_buttons()
        if self.run.buttons:
            self.run.btn_dict = dict(zip(self.run.buttons, self.run.btn_class))

    def set_buttons(self):
        def offset_button(top_left):
            padding = 80
            top_left[1] += padding
            return top_left

        btn_width, btn_height = 100, 50
        top_left = [WIDTH // 2 - btn_width // 2, btn_height]
        dimensions = (btn_width, btn_height)
        button = pg.Rect(top_left, dimensions)
        for btn_name in self.run.btn_names:
            btn = gui.elements.UIButton(relative_rect=button,
                                        text=btn_name,
                                        manager=self.run.manager)
            self.run.buttons.append(btn)
            button = pg.Rect(offset_button(top_left), dimensions)
