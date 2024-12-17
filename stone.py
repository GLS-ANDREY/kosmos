import random

import pygame

stone = pygame.image.load("pics/Meteorit.png")
transform_stown = pygame.transform.scale(stone, [50, 50])

def made_stone(x_stone, y_stone):
    stone_slovar = {"coord": [x_stone, y_stone], "speed_x": random.randint(-3, 3), "speed_y": random.randint(2, 3)}
    while stone_slovar["speed_x"] == 0 or stone_slovar["speed_x"] == -1 or stone_slovar["speed_x"] == 1:
        stone_slovar["speed_x"] = random.randint(-3, 3)
    return stone_slovar


def paint(stone, display: pygame.Surface):
    display.blit(transform_stown, stone["coord"])


def polet_stone(stone):
    stone["coord"][0] += stone["speed_x"]
    stone["coord"][1] += stone["speed_y"]
