import pygame as pg 

current_player_event = None

def get_distance_from(object1, object2):
    x1, y1 = object1.position[0], object1.position[1]
    x2, y2 = object2.position[0], object2.position[1]
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

def in_range(object1, object2, range_in_tiles):
    distance = get_distance_from(object1, object2)
    return distance <= range_in_tiles * 64

def update_player_inputs(current_event):
    if current_event.type == pg.KEYDOWN:
        current_player_event = "KEYDOWN"
    
    if current_event.type == pg.MOUSEBUTTONDOWN:
        current_player_event = "MOUSEBUTTONDOWN"