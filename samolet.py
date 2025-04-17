import pygame, random, bullet, messenger, points,stone,animation

def paint(display: pygame.Surface, otladka):
    display.blit(transform_samolet, samolet_slovar["coord"])
    animation.animation_pics(samolet_slovar["fire"],display)

    if otladka:
        for all_rect in samolet_slovar["hit_rect"]:
            pygame.draw.rect(display, [255, 100, 255], all_rect, 2)


def dvizhenie_vpravo(all_stone):
    _dvizhenie(0,25,all_stone)


def dvizhenie_vlevo(all_stone):
    _dvizhenie(0,-25,all_stone)


def dvizhenie_vniz(all_stone):
    _dvizhenie(1,25,all_stone)


def dvizhenie_vverx(all_stone):
    _dvizhenie(1,-25,all_stone)


def _dvizhenie(coordinata, chislo,all_stone):
    for one_stone in all_stone:
        stone.stone_popal_po_samoletu(one_stone, samolet_slovar)
    sscc_do = samolet_slovar["coord"][coordinata]
    samolet_slovar["coord"][coordinata] += chislo
    _granica_ekrana()
    sscc_posle = samolet_slovar["coord"][coordinata]
    sscc_pd = sscc_posle-sscc_do
    for all_rect in samolet_slovar["hit_rect"]:
        all_rect[coordinata] += sscc_pd

def controller(events):
    animation.controller(samolet_slovar["fire"],events)
    samolet_slovar["fire"]["coord"] = [samolet_slovar["coord"][0],samolet_slovar["coord"][1]]
#TODO: Сделали что бы появлялся огонь на самолете, посмотреть почему он не слушается времени которое выстовляем на последней строке этого модуля

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

samolet = pygame.image.load("pics/samolet.png")
transform_samolet = pygame.transform.scale(samolet, [149, 147])
samolet_slovar = {"coord": pygame.Rect([775, 843, 149, 147]),
                  "hit_rect": [pygame.Rect([835,845,30,32]),#нос
                               pygame.Rect(850, 877, 25, 55),#правое верхнее
                               pygame.Rect(825, 877, 25, 55),#левое верхнее

                               pygame.Rect(900, 950, 25, 25),#самое правое нижнее
                               pygame.Rect(880, 920, 20, 60),#чутка левее от самого правого нижнего (турбина)
                               pygame.Rect(850, 930, 30, 63),#делит центр (чутка левее от предыдущего)

                               pygame.Rect(775, 950, 25, 25),#самое левое нижнее
                               pygame.Rect(800, 920, 20, 60),#чутка правее от самого левого нижнего (турбина)
                               pygame.Rect(820, 930, 30, 63)]}#делит центр (чутка правее от предыдущего)
samolet_slovar["fire"] = animation.made_animation(500,500,"pics/fire",200,2000)
