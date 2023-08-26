from common import COLORS, HEIGHT, WIDTH, FPS
from pygame_gui.core.interfaces.manager_interface import IUIManagerInterface


class Game:
    def __init__(self, run):
        self.run = run
        print("Game starting.")
        self.run.manager.clear_and_reset()
        self.run.background.fill(COLORS["aqua"])
