import pygame, model, random

pygame.key.set_repeat(10)


def allsobitiya():
    s = pygame.event.get()

    for a in s:
        if a.type == pygame.QUIT:
            exit()

        if a.type == pygame.KEYDOWN and a.key == pygame.K_RIGHT:
            model.samolet_slovar["coord"][0] += 5
        if a.type == pygame.KEYDOWN and a.key == pygame.K_LEFT:
            model.samolet_slovar["coord"][0] -= 5
