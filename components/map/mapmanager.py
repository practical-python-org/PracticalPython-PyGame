import pygame as pg
import pygame_gui

"""
Map Manager class is responsible for creating, editing, saving and loading maps. 

Future features:
- Map editor
- Object creator
- Object deleter
- Map saver
- Map loader
- UI for all of the above
"""
class MapManager:

    def __init__(self, window_surface, tile_size, vertical_tile_num, horizontal_tile_num):
        self.window_surface = window_surface
        self.tile_size = tile_size
        self.vertical_tile_num = vertical_tile_num
        self.horizontal_tile_num = horizontal_tile_num
        self.height = self.vertical_tile_num * self.tile_size
        self.width = self.horizontal_tile_num * self.tile_size

    def map_editor(self):
        pass

    def create_object(self):
        pass

    def delete_object(self):
        pass

    def save_map(self):
        pass

    def load_map(self):
        pass

    def draw_tile_grid(self):
        for x in range(0, self.width, self.tile_size):
            pg.draw.line(self.window_surface, (255,0,0), (x, 0), (x, self.height))
        for y in range(0, self.height, self.tile_size):
            pg.draw.line(self.window_surface, (255,0,0), (0, y), (self.width, y))

    def update(self):
        pass