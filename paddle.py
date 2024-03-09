import pygame as pg


class Paddle(pg.sprite.Sprite):
    def __init__(self, screen: pg.Surface, position: pg.Vector2):
        pg.sprite.Sprite.__init__(self)
        self.screen = screen
        self.position_center = position

        self.color = "white"
        self.speed_x = 50
        self.height = 20
        self.width = 100
        self.width_middle = self.width // 2
        self.width_inter = self.width_middle // 2
        self.width_corners = self.height
        self.width_rect_paddle = self.width - self.width_corners
        self.offset_inter = self.width_middle // 2 + self.width_inter // 2
        self.offset_corner = self.offset_inter + self.width_inter // 2 + self.width_corners // 2

        self.middle = pg.Surface((self.width_middle, self.height))
        self.middle.fill("red")
        self.inter_l = pg.Surface((self.width_inter, self.height))
        self.inter_l.fill("orange")
        self.inter_r = pg.Surface((self.width_inter, self.height))
        self.inter_r.fill("orange")
        self.corner_l = pg.Surface((self.width_corners, self.height))
        self.corner_l.fill("yellow")
        self.corner_r = pg.Surface((self.width_corners, self.height))
        self.corner_r.fill("yellow")

        # this surface and rect is only for visual representation
        self.paddle = pg.Surface((self.width_rect_paddle, self.height))
        self.paddle.fill(self.color)
        self.rect_paddle = self.paddle.get_rect(center=(self.position_center.x, self.position_center.y))

        # these rects are used for collision detection
        self.rect_middle = self.middle.get_rect(center=(self.position_center.x, self.position_center.y))
        self.rect_inter_l = self.inter_l.get_rect(center=(self.position_center.x - self.offset_inter,
                                                          self.position_center.y))
        self.rect_inter_r = self.inter_r.get_rect(center=(self.position_center.x + self.offset_inter,
                                                          self.position_center.y))
        self.rect_corner_l = self.corner_l.get_rect(center=(self.position_center.x - self.offset_corner,
                                                            self.position_center.y))
        self.rect_corner_r = self.corner_r.get_rect(center=(self.position_center.x + self.offset_corner,
                                                            self.position_center.y))

    def update(self):
        self.position_center = pg.Vector2(pg.mouse.get_pos()[0], self.position_center.y)
        self.rect_paddle.center = (self.position_center.x, self.position_center.y)
        self.rect_middle.center = (self.position_center.x, self.position_center.y)
        self.rect_inter_l.center = (self.position_center.x - self.offset_inter, self.position_center.y)
        self.rect_inter_r.center = (self.position_center.x + self.offset_inter, self.position_center.y)
        self.rect_corner_l.center = (self.position_center.x - self.offset_corner, self.position_center.y)
        self.rect_corner_r.center = (self.position_center.x + self.offset_corner, self.position_center.y)

        # the paddle's actual visual representation
        pg.draw.rect(self.screen, self.color, self.rect_paddle)
        pg.draw.circle(self.screen, self.color, self.rect_corner_l.center, self.width_corners//2)
        pg.draw.circle(self.screen, self.color, self.rect_corner_r.center, self.width_corners//2)

        # debug visualization of the paddle's collision zones
        self.screen.blit(self.middle, self.rect_middle)
        self.screen.blit(self.inter_l, self.rect_inter_l)
        self.screen.blit(self.inter_r, self.rect_inter_r)
        self.screen.blit(self.corner_l, self.rect_corner_l)
        self.screen.blit(self.corner_r, self.rect_corner_r)
