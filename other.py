from common import COLORS, HEIGHT, WIDTH, FPS


class Other:

    def __init__(self, run):
        self.run = run
        print("Hello from the other side.")
        self.run.manager.clear_and_reset()
        self.run.background.fill(COLORS["yellowgreen"])
