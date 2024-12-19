import pygame, model, random,stone,bullet

pygame.init()

samolet = pygame.image.load("pics/samolet.png")
fon = pygame.image.load("pics/fon.png")

transform_samolet = pygame.transform.scale(samolet, [149, 147])
transform_fon = pygame.transform.scale(fon, [1700, 1000])

font = pygame.font.SysFont("arial", 20, True)

display = pygame.display.set_mode([1700, 1000])


def risovanie():
    display.fill([0, 0, 0])

    display.blit(transform_fon, [0, 0])
    display.blit(transform_samolet, model.samolet_slovar["coord"])
    for infa_stone in model.all_stone:
        stone.paint(infa_stone, display)

    for infa_bullet in model.all_bullet:
        bullet.paint(infa_bullet, display)

    pygame.display.flip()
