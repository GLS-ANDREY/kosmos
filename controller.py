import pygame, model, random, bullet

import stown

pygame.key.set_repeat(10)

dvizhenie_puli = pygame.event.custom_type()
pygame.time.set_timer(dvizhenie_puli, 10)

dvizhenie_stown = pygame.event.custom_type()
pygame.time.set_timer(dvizhenie_stown, 10)

spawn_stown = pygame.event.custom_type()
pygame.time.set_timer(spawn_stown,3000)


def allsobitiya():
    s = pygame.event.get()

    for a in s:
        if a.type == pygame.QUIT:
            exit()

        if a.type == spawn_stown:
            stown_slovar = stown.made_stown(random.randint(700, 900), -70)
            model.all_stown.append(stown_slovar)

        if a.type == dvizhenie_puli:
            for infa_bullet in model.all_bullet:
                bullet.polet_pul(infa_bullet)

        if a.type == dvizhenie_stown:
            for infa_stown in model.all_stown:
                stown.polet_stown(infa_stown)

        if a.type == pygame.MOUSEBUTTONDOWN and (a.button == pygame.BUTTON_RIGHT or a.button == pygame.BUTTON_LEFT):
            if a.button == pygame.BUTTON_RIGHT:
                button = "right"
            else:
                button = "left"
            model.strelba(button)

        if a.type == pygame.KEYDOWN and a.key == pygame.K_d:
            model.samolet_slovar["coord"][0] += 15
            model.granica_ekrana()

        if a.type == pygame.KEYDOWN and a.key == pygame.K_a:
            model.samolet_slovar["coord"][0] -= 15
            model.granica_ekrana()

        if a.type == pygame.KEYDOWN and a.key == pygame.K_s:
            model.samolet_slovar["coord"][1] += 15
            model.granica_ekrana()

        if a.type == pygame.KEYDOWN and a.key == pygame.K_w:
            model.samolet_slovar["coord"][1] -= 15
            model.granica_ekrana()
