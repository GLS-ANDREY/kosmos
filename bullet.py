#ПОЖАРНАЯ ТРЕВОГА С САВОЙ
import pygame

bullet = pygame.image.load("pics/bullet.png")
transform_bullet = pygame.transform.scale(bullet, [6, 21])


def made_bullet(x_bullet,y_bullet):
    return {"coord": [x_bullet,y_bullet]}
def paint(bullet,display:pygame.Surface):
    display.blit(transform_bullet,bullet["coord"])