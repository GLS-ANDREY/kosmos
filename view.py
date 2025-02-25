import pygame, model, random, stone, bullet,hp_bar,sounds,points

import gift_hp
import samolet

pygame.init()

fon = pygame.image.load("pics/fon.png")
sound_off = pygame.image.load("pics/off_sound.png")

transform_fon = pygame.transform.scale(fon, [1700, 1000])
transform_sound_off = pygame.transform.scale(sound_off, [70,70])

font = pygame.font.SysFont("arial", 20, True)

display = pygame.display.set_mode([1700, 1000])


def risovanie():
    display.fill([0, 0, 0])

    display.blit(transform_fon, [0, 0])
    if sounds.sound_off_on == 0:
        display.blit(transform_sound_off,[1630,60])
    for infa_stone in model.all_stone:
        stone.paint(infa_stone, display)

    for infa_bullet in model.all_bullet:
        bullet.paint(infa_bullet, display)

    for infa_gift in model.all_gifts:
        gift_hp.paint(infa_gift,display)


    points.paint(display)

    hp_bar.paint(display)

    samolet.paint(display,model.otladka)

    pygame.display.flip()
