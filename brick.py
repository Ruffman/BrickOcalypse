import pygame as pg
import editor


WIDTH = 100
HEIGHT = 30




class Brick(pg.sprite.Sprite):
    def __init__(self, screen: pg.Surface, position: pg.Vector2, level: int):
        pg.sprite.Sprite.__init__(self)
        self.screen = screen

        self.position = position
        self.level = level
        self.color = editor.BRICK_LVL_TO_COLOR[level]

        self.image = pg.Surface([WIDTH, HEIGHT])
        self.image.fill(self.color)

        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))

    def update(self):
        self.screen.blit(self.image, self.rect)

    def change_color(self, color):
        self.color = color
        self.image.fill(self.color)
