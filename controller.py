import pygame, model, random, bullet,stone

import hp_bar
import sounds

pygame.key.set_repeat(10)

dvizhenie_puli = pygame.event.custom_type()
pygame.time.set_timer(dvizhenie_puli, 10)

dvizhenie_stone = pygame.event.custom_type()
pygame.time.set_timer(dvizhenie_stone, 10)

spawn_stone = pygame.event.custom_type()
pygame.time.set_timer(spawn_stone, 3000)

def allsobitiya():
    s = pygame.event.get()

    for a in s:
        if a.type == pygame.QUIT:
            exit()

        if a.type == spawn_stone:
            stone_slovar = stone.made_stone(random.randint(600, 900), -50)
            model.all_stone.append(stone_slovar)

        if a.type == dvizhenie_puli:
            for infa_bullet in model.all_bullet:
                bullet.polet_pul(infa_bullet,model.all_stone)

        if a.type == dvizhenie_stone:
            for infa_stone in model.all_stone:
                stone.polet_stone(infa_stone)

        if a.type == pygame.KEYUP and a.key == pygame.K_m:
            sounds.sound_off_on = 0.2 if sounds.sound_off_on == 0 else 0
            sounds.stone_break_sound.set_volume(sounds.sound_off_on)

        if a.type == pygame.MOUSEBUTTONDOWN and (a.button == pygame.BUTTON_RIGHT or a.button == pygame.BUTTON_LEFT):
            if a.button == pygame.BUTTON_RIGHT:
                button = "right"
            else:
                button = "left"
            model.strelba(button)

        if a.type == pygame.KEYDOWN and a.key == pygame.K_d:
            model.samolet_slovar["coord"][0] += 25
            model.granica_ekrana()

        if a.type == pygame.KEYDOWN and a.key == pygame.K_a:
            model.samolet_slovar["coord"][0] -= 25
            model.granica_ekrana()

        if a.type == pygame.KEYDOWN and a.key == pygame.K_s:
            model.samolet_slovar["coord"][1] += 25
            model.granica_ekrana()

        if a.type == pygame.KEYDOWN and a.key == pygame.K_w:
            model.samolet_slovar["coord"][1] -= 25
            model.granica_ekrana()
