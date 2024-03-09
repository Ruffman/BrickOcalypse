import pygame as pg


WIDTH = 100
HEIGHT = 30

HEALTH_CODES = {
    1: "white",
    2: "red",
    3: "orange",
    4: "yellow",
    5: "green",
}


class Brick(pg.sprite.Sprite):
    def __init__(self, screen: pg.Surface, position: pg.Vector2, level: int):
        pg.sprite.Sprite.__init__(self)
        self.screen = screen

        self.position = position
        self.level = level
        self.color = HEALTH_CODES[level]

        self.image = pg.Surface([WIDTH, HEIGHT])
        self.image.fill(self.color)

        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))

    def update(self):
        self.screen.blit(self.image, self.rect)

    def change_color(self, color):
        self.color = color
        self.image.fill(self.color)
