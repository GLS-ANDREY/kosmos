import pygame, model, random

pygame.key.set_repeat(10)

def allsobitiya():
    s = pygame.event.get()

    for a in s:
        if a.type == pygame.QUIT:
            exit()

