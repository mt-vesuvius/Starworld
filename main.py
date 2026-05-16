import pygame as pg
from Scripts.Objects import *


# GAME INFO
TITLE = "Starworld"
VERSION = "0.1"

pg.init()
screen = pg.display.set_mode((1280, 640))
pg.display.set_caption(TITLE + " v" + VERSION)
clock = pg.time.Clock()
running = True

TILESIZE = 64

player = Player(0, 0)
tree1 = Tree(128, 256, 3)
tree2 = Tree(512, 512, 4)

while running:

    # GET PYGAME EVENTS
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                player.move("UP")
            elif event.key == pg.K_s:
                player.move("DOWN")

            if event.key == pg.K_a:
                player.move("LEFT")
            elif event.key == pg.K_d:
                player.move("RIGHT")

    # wipe screen
    screen.fill("PURPLE")

    # RENDER GAME HERE

    tree1.render(screen)    # we can make a tree spawner after we have collisions
    tree2.render(screen)    # and also tilemaps / world generation so we don't have to manually spawn them
    player.render(screen)

    # render to screen
    pg.display.flip()

    clock.tick(60)

pg.quit()
