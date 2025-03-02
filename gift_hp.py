import pygame,random,samolet,messenger

import image_helpers


def made_gift():
    x_gift = random.randint(50,1650)
    gift_slovar = {"coord": pygame.Rect(x_gift, -70, 42, 42), "speed_y": 3}
    return gift_slovar

def paint(gift,display:pygame.Surface, otladka):
    display.blit(parashut_surface,[gift["coord"].x-25,gift["coord"].y-75])
    display.blit(gift_surface,gift["coord"])
    if otladka:
        pygame.draw.rect(display,[255,255,255],gift["coord"],2)

def collect_gift(gift):
    sbor_podarka = gift["coord"].collidelist(samolet.samolet_slovar["hit_rect"])
    if sbor_podarka != -1:
        messenger.send_message("Самолет собрал подарок",gift)

def polet_gifta(gift):
    gift["coord"].y += gift["speed_y"]
    gift["speed_y"] -= 0.003
    if gift["coord"].y >= 965:
        gift["speed_y"] -= 10
    if gift["speed_y"] > 0:
        collect_gift(gift)


gift_surface = image_helpers.helper_load("pics/Chest.png",40,40)
parashut_surface = image_helpers.helper_load("pics/parashut.png",90,90)
