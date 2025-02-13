import pygame,random

def made_gift():
    x_gift = random.randint(50,1650)
    gift_slovar = {"coord": pygame.Rect(x_gift, 70, 50, 50)}
    return gift_slovar

def paint(gift ,display:pygame.Surface):
    display.blit(transform_gift, [gift["coord"].x,gift["coord"].y])

def _polet_gifta():
    speed_x = 3
    speed_y = 3


gift = pygame.image.load("pics/Chest.png")
transform_gift = pygame.transform.scale(gift,[40,40])