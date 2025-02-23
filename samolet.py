import pygame, random, bullet, messenger, points, model

samolet = pygame.image.load("pics/samolet.png")
transform_samolet = pygame.transform.scale(samolet, [149, 147])
samolet_slovar = {"coord": pygame.Rect([775, 843, 149, 147]),
                  "hit_rect": [pygame.Rect(820, 843, 60, 147), pygame.Rect(775, 925, 149, 65)]}


def paint(display: pygame.Surface):
    display.blit(transform_samolet, samolet_slovar["coord"])
    for all_rect in samolet_slovar["hit_rect"]:
        pygame.draw.rect(display, [255, 100, 255], all_rect, 2)


def dvizhenie_vpravo():
    _dvizhenie(0,25)


def dvizhenie_vlevo():
    _dvizhenie(0,-25)


def dvizhenie_vniz():
    _dvizhenie(1,25)


def dvizhenie_vverx():
    _dvizhenie(1,-25)

def _dvizhenie(coordinata, chislo):
    sscc_do = samolet_slovar["coord"][coordinata]
    samolet_slovar["coord"][coordinata] += chislo
    _granica_ekrana()
    sscc_posle = samolet_slovar["coord"][coordinata]
    sscc_pd = sscc_posle-sscc_do
    for all_rect in samolet_slovar["hit_rect"]:
        all_rect[coordinata] += sscc_pd



def strelba(button_r_or_l=None):
    coord_bullet_x = 30 if button_r_or_l == "left" else 115
    bullet_slovar = bullet.made_bullet(samolet_slovar["coord"][0] + coord_bullet_x, samolet_slovar["coord"][1] + 50)
    return bullet_slovar


# TODO:Приедлать к честу парашют, если камень попадает по самолету -хп, cделать режим отладки по кнопке

def _granica_ekrana():
    if samolet_slovar["coord"][0] <= 0:
        samolet_slovar["coord"][0] = 0

    if samolet_slovar["coord"][0] >= 1551:
        samolet_slovar["coord"][0] = 1551

    if samolet_slovar["coord"][1] >= 843:
        samolet_slovar["coord"][1] = 843

    if samolet_slovar["coord"][1] <= 0:
        samolet_slovar["coord"][1] = 0
