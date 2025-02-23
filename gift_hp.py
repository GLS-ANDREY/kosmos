import pygame,random

import messenger
import samolet

def made_gift():
    x_gift = random.randint(50,1650)
    gift_slovar = {"coord": pygame.Rect(x_gift, -70, 45, 45)}
    return gift_slovar

def paint(gift ,display:pygame.Surface):
    pygame.draw.rect(display,[255,255,255],gift["coord"],2)


def collect_chest(gift):
    sbor_podarka = gift["coord"].collidelist(samolet.samolet_slovar["hit_rect"])
    if sbor_podarka != -1:
        messenger.send_message("Самолет собрал подарок",gift)

def polet_gifta(gift):
    speed_y = 3
    gift["coord"].y += speed_y
    collect_chest(gift)



gift = pygame.image.load("pics/Chest.png")
transform_gift = pygame.transform.scale(gift,[40,40])