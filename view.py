import pygame, model, random

pygame.init()

font = pygame.font.SysFont("arial", 20, True)

display = pygame.display.set_mode([1700, 1000])

def risovanie():
    display.fill([0, 0, 0])
    pygame.display.flip()
