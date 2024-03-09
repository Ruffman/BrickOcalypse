import pygame as pg

from ball import Ball
from playboard import Playboard
from paddle import Paddle
import editor


FPS = 60
WIDTH = 1280
HEIGHT = 720


def handle_ball_coll_border():
    radius = my_ball.radius // 2
    if 0 + radius > my_ball.position.x or my_ball.position.x > my_playboard.width - radius:
        my_ball.speed_x *= -1
    if 0 + radius > my_ball.position.y or my_ball.position.y > my_playboard.height - radius:
        my_ball.speed_y *= -1


def player_paddle_with_ball_collision_check():
    if my_ball.rect.colliderect(player_paddle.rect):
        my_ball.speed_y *= -1


# pygame setup
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.mouse.set_visible(editor.EDITOR_MODE)
running = True
dt = 0

my_ball = Ball(screen, position=pg.Vector2(WIDTH // 2, HEIGHT // 2))
player_paddle = Paddle(screen, pg.Vector2(WIDTH // 2, HEIGHT - 60))
my_playboard = Playboard(WIDTH, HEIGHT)

my_playboard.calc_grid_coord()


def toggle_edit_mode():
    editor.EDITOR_MODE = not editor.EDITOR_MODE
    pg.mouse.set_visible(editor.EDITOR_MODE)
    my_playboard.edit_mode = editor.EDITOR_MODE



def play_game():
    # logic updates HERE
    handle_ball_coll_border()
    player_paddle_with_ball_collision_check()
    for i in range(0, len(my_playboard.bricks) - 1):
        if my_ball.rect.colliderect(my_playboard.bricks[i].rect):
            my_playboard.bricks.pop(i)

    # RENDER YOUR GAME HERE
    my_playboard.update(screen)

    if not editor.EDITOR_MODE:
        my_ball.update(dt)
        player_paddle.update()


while running:
    # poll for events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            button = event.dict['button']
            if editor.EDITOR_MODE:
                if button == 1:
                    my_playboard.add_brick(editor.NEW_BRICK_LVL)
                if button == 3:
                    my_playboard.delete_brick()
        if event.type == pg.KEYDOWN:
            key = event.dict['key']
            if key == pg.K_RIGHT:
                my_playboard.increase_cell_width()
            if key == pg.K_LEFT:
                my_playboard.decrease_cell_width()
            if key == pg.K_UP:
                my_playboard.increase_cell_height()
            if key == pg.K_DOWN:
                my_playboard.decrease_cell_height()
            if key == pg.K_s:
                my_playboard.save_brick_layout()
            if key == pg.K_l:
                my_playboard.load_brick_layout()
            if key == pg.K_e:
                toggle_edit_mode()


    play_game()

    # flip() the display to put your work on screen
    pg.display.flip()

    # limits FPS to 60
    # dt is the time in ms since last frame
    dt = clock.tick(FPS) / 1000

pg.quit()
