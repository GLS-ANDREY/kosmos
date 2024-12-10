import pygame, model, random

pygame.init()

samolet = pygame.image.load("pics/samolet.png")
fon = pygame.image.load("pics/fon.png")
pulya = pygame.image.load("pics/bullet.png")

transform_samolet = pygame.transform.scale(samolet, [149, 147])
transform_fon = pygame.transform.scale(fon, [1700, 1000])
transform_pulya = pygame.transform.scale(pulya, [6, 21])

font = pygame.font.SysFont("arial", 20, True)

display = pygame.display.set_mode([1700, 1000])


def risovanie():
    display.fill([0, 0, 0])

    display.blit(transform_fon, [0, 0])
    display.blit(transform_samolet, model.samolet_slovar["coord"])

    for infa_bullet in model.all_bullet:
        display.blit(transform_pulya, [infa_bullet["coord"][0], infa_bullet["coord"][1]])

    pygame.display.flip()

