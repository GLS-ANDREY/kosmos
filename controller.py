import pygame, model, random

pygame.key.set_repeat(10)


def allsobitiya():
    s = pygame.event.get()

    for a in s:
        if a.type == pygame.QUIT:
            exit()

        if a.type == pygame.MOUSEBUTTONDOWN and a.button == pygame.BUTTON_LEFT:
            bullet_slovar = {"coord": [random.randint(100, 1000), random.randint(100, 800)]}
            model.all_bullet.append(bullet_slovar)
            model.strelba_left()
        # if a.type == pygame.MOUSEBUTTONDOWN and a.button == pygame.BUTTON_RIGHT:

        if a.type == pygame.KEYDOWN and a.key == pygame.K_d:
            model.samolet_slovar["coord"][0] += 5
            model.granica_ekrana()

        if a.type == pygame.KEYDOWN and a.key == pygame.K_a:
            model.samolet_slovar["coord"][0] -= 5
            model.granica_ekrana()

        if a.type == pygame.KEYDOWN and a.key == pygame.K_s:
            model.samolet_slovar["coord"][1] += 5
            model.granica_ekrana()

        if a.type == pygame.KEYDOWN and a.key == pygame.K_w:
            model.samolet_slovar["coord"][1] -= 5
            model.granica_ekrana()
