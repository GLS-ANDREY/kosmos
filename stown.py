import random

import pygame

stown = pygame.image.load("pics/Meteorit.png")
transform_stown = pygame.transform.scale(stown, [50, 50])


def made_stown(x_stown, y_stown):
    #TODO: Сделать что бы не было стоячих камней(сделать иф в котором говорится if stown["speed_x"] == 0: stown["speed_x"] = random.randint(-3, 3), и так же с 1 и -1, сделать поворот камня

    return {"coord": [x_stown, y_stown], "speed_x": random.randint(-3,3), "speed_y": random.randint(2,3)}

def paint(stown, display: pygame.Surface):
    display.blit(transform_stown, stown["coord"])

def polet_stown(stown):
    stown["coord"][0] += stown["speed_x"]
    stown["coord"][1] += stown["speed_y"]
