import pygame as pg

TILESIZE = 64

class Player:
    def __init__(self, x, y):
        self.position = [x, y]
        self.hitbox = (64, 64)
        self.currentSprite = 0
        self.facing = "RIGHT"

        #create a list of sprites, one facing each direction

    def move(self, direction):
        if direction == "UP":
            self.position[1] -= TILESIZE
            self.facing = "UP"
        elif direction == "DOWN":
            self.position[1] += TILESIZE
            self.facing = "DOWN"
        elif direction == "LEFT":
            self.position[0] -= TILESIZE
            self.facing = "LEFT"
        elif direction == "RIGHT":
            self.position[0] += TILESIZE
            self.facing = "RIGHT"
    
    def render(self, screen):
        pg.draw.rect(screen, "RED", (self.position[0], self.position[1], self.hitbox[0], self.hitbox[1]))