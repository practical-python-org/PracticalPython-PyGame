import pygame as pg
import matplotlib.colors as mcl

# Colors
COLORS: dict = mcl.CSS4_COLORS

# Tiles and Screen
TILE_SIZE = 64
VERTICAL_TILE_NUM = 10
HORIZONTAL_TILE_NUM = 12

HEIGHT = VERTICAL_TILE_NUM * TILE_SIZE
WIDTH = HORIZONTAL_TILE_NUM * TILE_SIZE

# Time
FPS = 60
