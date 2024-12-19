import pygame, random,bullet


all_bullet = []
all_stone = []
samolet_slovar = {"coord": [775, 843]}


def granica_ekrana():
    if samolet_slovar["coord"][0] <= 0:
        samolet_slovar["coord"][0] = 0

    if samolet_slovar["coord"][0] >= 1551:
        samolet_slovar["coord"][0] = 1551

    if samolet_slovar["coord"][1] >= 843:
        samolet_slovar["coord"][1] = 843

    if samolet_slovar["coord"][1] <= 0:
        samolet_slovar["coord"][1] = 0


def strelba(button_r_or_l):
    coord_bullet_x = 30 if button_r_or_l == "left" else 115
    bullet_slovar = bullet.made_bullet(samolet_slovar["coord"][0] + coord_bullet_x, samolet_slovar["coord"][1] + 50)
    all_bullet.append(bullet_slovar)
