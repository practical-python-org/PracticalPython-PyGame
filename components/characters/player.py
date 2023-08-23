import pygame as pg

class Player:

    def __init__(self, screen, x, y, width, height):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.create_player()
        self.move_player()
        
    def create_player(self):
        pg.draw.rect(self.screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def player_information_logger(self):
        print("Player information: {}".format(self.__dict__))
        print(self.screen.get_size())

    def move_player(self):
        
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.x -= 1
        if keys[pg.K_RIGHT]:
            self.x += 1
        if keys[pg.K_UP]:
            self.y -= 1
        if keys[pg.K_DOWN]:
            self.y += 1

    def update(self):
        self.create_player()
        self.move_player()
        pg.display.update()
