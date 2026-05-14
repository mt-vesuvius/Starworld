import pygame as pg

TILESIZE = 64

class Player:
    def __init__(self, x, y):
        self.position = [x, y]
        self.hitbox = (64, 64)

    def move(self, direction):
        if direction == "UP":
            self.position[1] -= TILESIZE
        elif direction == "DOWN":
            self.position[1] += TILESIZE
        elif direction == "LEFT":
            self.position[0] -= TILESIZE
        elif direction == "RIGHT":
            self.position[0] += TILESIZE
    
    def render(self, screen):
        pg.draw.rect(screen, "RED", (self.position[0], self.position[1], self.hitbox[0], self.hitbox[1]))