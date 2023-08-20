"""
Taken directly from https://pygame-gui.readthedocs.io/en/latest/quick_start.html as a template.
"""
import pygame
import pygame_gui


class RunGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.bkgd_color = pygame.Color('#000000')

        pygame.init()

        pygame.display.set_caption('Quick Start')
        self.window_surface = pygame.display.set_mode((self.width, self.height))

        self.background = pygame.Surface((self.width, self.height))
        #
        self.background.fill(self.bkgd_color)

        self.manager = pygame_gui.UIManager((self.width, self.height))

        self.rectangle = pygame.Rect((350, 275), (100, 50))
        self.hello_button = pygame_gui.elements.UIButton(relative_rect=self.rectangle,
                                                         text='Say Hello',
                                                         manager=self.manager)
        self.game_loop()

    def game_loop(self):
        clock = pygame.time.Clock()
        is_running = True

        while is_running:
            time_delta = clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.hello_button:
                        print('Hello World!')

                self.manager.process_events(event)

            self.manager.update(time_delta)

            self.window_surface.blit(self.background, (0, 0))
            self.manager.draw_ui(self.window_surface)

            pygame.display.update()


width, height = 800, 600
RunGame(width, height)
