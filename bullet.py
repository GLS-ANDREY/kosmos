import pygame

import model

def made_bullet(x_bullet, y_bullet):
    return {"coord": pygame.Rect(x_bullet, y_bullet, 6, 21)}


def paint(bullet, display: pygame.Surface,stone=None):
    display.blit(transform_bullet, bullet["coord"])
    # pygame.draw.rect(display, [255,255,255],[bullet["coord"][0],bullet["coord"][1],6,21],1)

def del_stone(bullet,stone=None):
    if type(stone) == list:
        for collide_stone in stone:
            collide_t_or_f = bullet["coord"].colliderect(collide_stone["coord"])
            if collide_t_or_f == True:
                model.all_stone.remove(collide_stone)


def polet_pul(bullet,stone):
    bullet["coord"].y -= 5
    del_stone(bullet,stone)

bullet = pygame.image.load("pics/bullet.png")
transform_bullet = pygame.transform.scale(bullet, [6, 21])
