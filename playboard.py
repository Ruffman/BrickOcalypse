import pygame as pg

import editor
from brick import Brick
import math
import json



class Playboard:
    def __init__(self, width, height):
        self.edit_mode = True
        self.width = width
        self.height = height

        self.cell_width = 110
        self.cell_height = 40
        self.padding_x = 140
        self.padding_y = 40
        self.grid_coord = []
        self.active_coord = (0, 0)

        self.surface = pg.Surface((self.width, self.height))

        self.bricks: list[Brick] = []
        self.num_bricks = 0

        self.player_balls = 3
        self.game_is_on = True

        self.font = pg.font.SysFont("Comic Sans MS", 20)

    def display_num_bricks(self):
        label = self.font.render(f"Bricks left: {len(self.bricks)}/{self.num_bricks}", 1, "white")
        self.surface.blit(label, (30, 10))

    def display_num_lives(self):
        label = self.font.render(f"Balls left: {self.player_balls}", 1, "white")
        self.surface.blit(label, (1100, 10))

    def add_brick(self, level: int):
        is_free = True
        if level not in editor.BRICK_LVL_TO_COLOR:
            return

        for brick in self.bricks:
            if brick.position == self.active_coord:
                is_free = False
        if is_free:
            self.bricks.append(Brick(self.surface, pg.Vector2(self.active_coord), level))

    def delete_brick(self):
        brick_exists = False
        brick_index = -1
        for brick in self.bricks:
            if brick.position == self.active_coord:
                brick_exists = True
                brick_index = self.bricks.index(brick)
        if brick_exists:
            self.bricks.pop(brick_index)

    def save_brick_layout(self):
        layout_data = {"bricks": [
            {"x": brick.position.x, "y": brick.position.y, "level": brick.level} for brick in self.bricks
        ]}

        with open("maps/data.json", "w", encoding="utf-8") as file:
            json.dump(layout_data, file, ensure_ascii=False, indent=4)

    def load_brick_layout(self):
        with open("maps/data.json", "r") as file:
            layout_data = json.load(file)
            for brick in layout_data["bricks"]:
                self.bricks.append(Brick(self.surface, pg.Vector2(brick["x"], brick["y"]), brick["level"]))

        self.num_bricks = len(self.bricks)

    def display_game_win(self):
        font = pg.font.SysFont("Comic Sans MS", 30)
        label = font.render("You win!", 1, "white")
        self.surface.blit(label, (self.width // 2, self.height // 2))

    def display_game_loss(self):
        font = pg.font.SysFont("Comic Sans MS", 30)
        label = font.render("You lose!", 1, "white")
        self.surface.blit(label, (self.width // 2, self.height // 2))

    def update(self, screen: pg.Surface):
        self.surface.fill("black")

        for brick in self.bricks:
            brick.update()

        if self.edit_mode:
            self.paint_grid()
            self.find_active()
            self.highlight_active()

        self.display_num_bricks()
        self.display_num_lives()
        if len(self.bricks) == 0:
            self.game_is_on = False
            self.display_game_win()
        if self.player_balls == 0:
            self.game_is_on = False
            self.display_game_loss()
        screen.blit(self.surface, self.surface.get_rect())

    def calc_grid_coord(self):
        self.grid_coord = []
        start_x = 0
        start_y = 0

        start_y += self.padding_y
        start_y -= self.cell_height
        while start_y < self.height - self.padding_y * 5:
            start_x += self.padding_x
            start_x -= self.cell_width
            start_y += self.cell_height

            row_done = False
            while not row_done:
                start_x += self.cell_width
                if start_x > self.width - self.padding_x:
                    row_done = True
                    start_x = 0
                else:
                    self.grid_coord.append((start_x, start_y))

    def paint_grid(self):
        for c in self.grid_coord:
            pg.draw.circle(self.surface, "white", c, 1)

    def find_active(self):
        mouse_c = pg.mouse.get_pos()
        shortest_dist = 1000
        for index, c in enumerate(self.grid_coord):
            dist = math.sqrt((mouse_c[0] - c[0]) ** 2 + (mouse_c[1] - c[1]) ** 2)
            if dist < shortest_dist:
                shortest_dist = dist
                self.active_coord = self.grid_coord[index]

    def highlight_active(self):
        pg.draw.circle(self.surface, "red", self.active_coord, 5)

    def increase_cell_width(self):
        self.cell_width += 5
        self.calc_grid_coord()

    def decrease_cell_width(self):
        self.cell_width -= 5
        if self.cell_width <= 0:
            self.cell_width = 5
        self.calc_grid_coord()

    def increase_cell_height(self):
        self.cell_height += 5
        self.calc_grid_coord()

    def decrease_cell_height(self):
        self.cell_height -= 5
        if self.cell_height <= 0:
            self.cell_height = 5
        self.calc_grid_coord()
