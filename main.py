"""
Taken directly from https://pygame-gui.readthedocs.io/en/latest/quick_start.html as a template.
"""
import pygame
import pygame_gui


class RunGame:
    BLACK = pygame.Color('#000000')

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.buttons = list()
        self.init_ui()
        self.game_loop()

    def set_buttons(self):
        def offset_button(top_left):
            padding = 80
            top_left[1] += padding
            print(top_left)
            return top_left

        btn_width, btn_height = 100, 50
        top_left = [self.width//2 - btn_width//2, btn_height]
        dimensions = [btn_width, btn_height]

        self.button = pygame.Rect(top_left, dimensions)
        self.btn_names = ['START', 'SETTINGS', 'OTHER']
        for btn_name in self.btn_names:
            print(top_left, dimensions)
            btn = pygame_gui.elements.UIButton(relative_rect=self.button,
                                               text=btn_name,
                                               manager=self.manager)
            self.buttons.append(btn)
            self.button = pygame.Rect(offset_button(top_left), dimensions)

    def init_ui(self):
        pygame.init()
        pygame.display.set_caption('Quick Start')
        self.window_surface = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface((self.width, self.height))
        self.background.fill(RunGame.BLACK)

        self.manager = pygame_gui.UIManager((self.width, self.height))

        self.set_buttons()

    def game_loop(self):
        clock = pygame.time.Clock()
        is_running = True

        while is_running:
            time_delta = clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    for btn in self.buttons:
                        if event.ui_element == btn:
                            print('Hello World!')

                self.manager.process_events(event)

            self.manager.update(time_delta)

            self.window_surface.blit(self.background, (0, 0))
            self.manager.draw_ui(self.window_surface)

            pygame.display.update()


width, height = 800, 600
RunGame(width, height)
