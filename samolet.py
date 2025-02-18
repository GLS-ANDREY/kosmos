import pygame, random,bullet,messenger,points,model

samolet = pygame.image.load("pics/samolet.png")
transform_samolet = pygame.transform.scale(samolet, [149, 147])
samolet_slovar = {"coord": [775, 843]}


def paint(display:pygame.Surface):
    display.blit(transform_samolet, samolet_slovar["coord"])



def dvizhenie_vpravo():
    samolet_slovar["coord"][0] += 25
    _granica_ekrana()

def dvizhenie_vlevo():
    samolet_slovar["coord"][0] -= 25
    _granica_ekrana()

def dvizhenie_vniz():
    samolet_slovar["coord"][1] += 25
    _granica_ekrana()

def dvizhenie_vverx():
    samolet_slovar["coord"][1] -= 25
    _granica_ekrana()


def strelba(button_r_or_l=None):
    coord_bullet_x = 30 if button_r_or_l == "left" else 115
    bullet_slovar = bullet.made_bullet(samolet_slovar["coord"][0] + coord_bullet_x, samolet_slovar["coord"][1] + 50)
    return bullet_slovar


def _granica_ekrana():
    if samolet_slovar["coord"][0] <= 0:
        samolet_slovar["coord"][0] = 0

    if samolet_slovar["coord"][0] >= 1551:
        samolet_slovar["coord"][0] = 1551

    if samolet_slovar["coord"][1] >= 843:
        samolet_slovar["coord"][1] = 843

    if samolet_slovar["coord"][1] <= 0:
        samolet_slovar["coord"][1] = 0
