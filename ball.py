import pygame as pg



class Ball(pg.sprite.Sprite):
    def __init__(self, screen: pg.Surface, position: pg.Vector2, color="white"):
        pg.sprite.Sprite.__init__(self)
        self.screen = screen
        self.color = color
        self.position = position

        self.radius = 20
        self.speed_x = -300
        self.speed_y = -300

        self.image = pg.Surface((self.radius, self.radius))
        self.image.fill("red")

        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))

    def update(self, delta_time):
        self.move(delta_time)
        self.screen.blit(self.image, self.rect)

    def move(self, delta_time):
        self.position.x += self.speed_x * delta_time
        self.position.y += self.speed_y * delta_time
        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))
