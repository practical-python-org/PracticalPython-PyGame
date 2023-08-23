import pygame as pg
import pygame_gui

"""
Map Manager class is responsible for creating, editing, saving and loading maps. 

Future features:
- Save and load maps from file
- Map editor
- Map editor UI
- Find better function names
"""
class MapManager:

    tiles = set()
    debug = False

    """
    MapManager constructor
    """
    def __init__(self, window_surface, tile_size, vertical_tile_num, horizontal_tile_num):
        self.window_surface = window_surface
        self.tile_size = tile_size
        self.vertical_tile_num = vertical_tile_num
        self.horizontal_tile_num = horizontal_tile_num
        self.height = self.vertical_tile_num * self.tile_size
        self.width = self.horizontal_tile_num * self.tile_size

    def map_editor(self):
        pass

    """
    Creates an object of type object_type at object_position
    """
    def render_object(self, object_type, object_position):
        if object_type == "tile":
            object_position_x = object_position[0] * self.tile_size 
            object_position_y = object_position[1] * self.tile_size
            object_dimensions = (self.tile_size, self.tile_size)
            pg.draw.rect(self.window_surface, (0, 255, 0), (object_position_x, object_position_y, object_dimensions[0], object_dimensions[1]))

    """
    Removes position from tiles set
    """
    def delete_object(self, object_position):
        if object_position in self.tiles:
            self.tiles.remove(object_position)

    """
    Saves position to tiles set
    """
    def save_map(self, object_position):
        self.tiles.add(object_position)

    """
    Returns tiles set
    """
    def load_map(self):
        return self.tiles

    """
    Draws debug grid on screen
    """
    def draw_tile_grid(self):
        for x in range(0, self.width, self.tile_size):
            pg.draw.line(self.window_surface, (255,0,0), (x, 0), (x, self.height))
        for y in range(0, self.height, self.tile_size):
            pg.draw.line(self.window_surface, (255,0,0), (0, y), (self.width, y))

    def enable_debug(self):
        self.debug = True

    def disable_debug(self):
        self.debug = False
