import pygame, model, random

pygame.key.set_repeat(10)
dvizhenie_puli = pygame.event.custom_type()
pygame.time.set_timer(dvizhenie_puli,10)

def allsobitiya():
    s = pygame.event.get()

    for a in s:
        if a.type == pygame.QUIT:
            exit()

        if a.type == pygame.KEYDOWN and a.key == pygame.K_SPACE:
            stown_slovar = {"coord": [random.randint(50,1500),random.randint(50,1000)]}
            model.all_stown.append(stown_slovar)

        if a.type == dvizhenie_puli:
            model.polet_pul()

        if a.type == pygame.MOUSEBUTTONDOWN and (a.button == pygame.BUTTON_RIGHT or a.button == pygame.BUTTON_LEFT):
            if a.button == pygame.BUTTON_RIGHT:
                button = "right"
            else:
                button = "left"
            model.strelba(button)

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
