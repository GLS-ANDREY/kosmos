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
    samolet_slovar["coord"][0] += 25
    for all_rect in samolet_slovar["hit_rect"]:
        all_rect[0] += 25
    _granica_ekrana()


def dvizhenie_vlevo():
    samolet_slovar["coord"][0] -= 25
    for all_rect in samolet_slovar["hit_rect"]:
        all_rect[0] -= 25
    _granica_ekrana()


def dvizhenie_vniz():
    samolet_slovar["coord"][1] += 25
    for all_rect in samolet_slovar["hit_rect"]:
        all_rect[1] += 25
    _granica_ekrana()


def dvizhenie_vverx():
    samolet_slovar["coord"][1] -= 25
    for all_rect in samolet_slovar["hit_rect"]:
        all_rect[1] -= 25
    _granica_ekrana()


def strelba(button_r_or_l=None):
    coord_bullet_x = 30 if button_r_or_l == "left" else 115
    bullet_slovar = bullet.made_bullet(samolet_slovar["coord"][0] + coord_bullet_x, samolet_slovar["coord"][1] + 50)
    return bullet_slovar


# TODO:Оживить честы, заменить картинку на парашют, если камень попадает по самолету -хп, cделать режим отладки по кнопке, сделать деф в котором будут парамерты координата([0]/[1])
# TODO: и знак([-1]/[1]), деф будет использоваться для движения

def _granica_ekrana():
    if samolet_slovar["coord"][0] <= 0:
        samolet_slovar["coord"][0] = 0

    if samolet_slovar["coord"][0] >= 1551:
        samolet_slovar["coord"][0] = 1551

    if samolet_slovar["coord"][1] >= 843:
        samolet_slovar["coord"][1] = 843

    if samolet_slovar["coord"][1] <= 0:
        samolet_slovar["coord"][1] = 0
