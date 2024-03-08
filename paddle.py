import pygame as pg


class Paddle(pg.sprite.Sprite):
    def __init__(self, screen: pg.Surface, position: pg.Vector2):
        pg.sprite.Sprite.__init__(self)
        self.screen = screen
        self.position = position

        self.color = "white"
        self.speed_x = 50
        self.width = 100
        self.height = 30

        self.image = pg.Surface((self.width, self.height))
        self.image.fill(self.color)

        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))

    def update(self):
        self.position = pg.Vector2(pg.mouse.get_pos()[0], self.position.y)
        self.rect.center = (self.position.x, self.position.y)
        self.screen.blit(self.image, self.rect)
