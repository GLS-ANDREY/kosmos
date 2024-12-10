import pygame, random

all_bullet = []

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

def strelba(coord_bullet_x):
    bullet_slovar = {"coord": [samolet_slovar["coord"][0] + coord_bullet_x, samolet_slovar["coord"][1] + 50]}
    all_bullet.append(bullet_slovar)