import pygame, random

sosdanie_puli_left = False
sosdanie_puli_right = False

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


def strelba_left():
    global sosdanie_puli_left
    sosdanie_puli_left = True

# def strelba_right():
#     global sosdanie_puli_right
#     sosdanie_puli_right = True

