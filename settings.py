from common import COLORS, HEIGHT, WIDTH, FPS


class Settings:

    def __init__(self, run):
        self.run = run
        print("Hello from settings.")
        self.run.manager.clear_and_reset()
        self.run.background.fill(COLORS["magenta"])
