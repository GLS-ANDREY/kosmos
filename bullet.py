import pygame

def made_bullet(x_bullet, y_bullet):
    return {"coord": pygame.Rect(x_bullet, y_bullet, 6, 21)}


def paint(bullet, display: pygame.Surface):
    display.blit(transform_bullet, bullet["coord"])
    bullet["coord"].colliderect()
    # pygame.draw.rect(display, [255,255,255],[bullet["coord"][0],bullet["coord"][1],6,21],1)


def polet_pul(bullet):
    bullet["coord"].y -= 5

bullet = pygame.image.load("pics/bullet.png")
transform_bullet = pygame.transform.scale(bullet, [6, 21])
