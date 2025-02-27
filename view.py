import pygame, model, random, stone, bullet,hp_bar,sounds,points

import gift_hp
import samolet


def helper_load():
    small_boom = pygame.image.load("pics/small_boom.png")
    transform_small_boom = pygame.transform.scale(small_boom,[24,24])
    return transform_small_boom


def paint():
    display.fill([0, 0, 0])
    display.blit(transform_fon, [0, 0])

    if sounds.sound_off_on == 0:
        display.blit(transform_sound_off,[1630,60])

    for infa_stone in model.all_stone:
        stone.paint(infa_stone, display,model.otladka)

    for infa_bullet in model.all_bullet:
        bullet.paint(infa_bullet, display, model.otladka)

    for infa_gift in model.all_gifts:
        gift_hp.paint(infa_gift,display, model.otladka)


    points.paint(display)

    hp_bar.paint(display)

    samolet.paint(display,model.otladka)

    display.blit(peremennaya_helper_load,[100,100])
    display.blit(transform_middle_boom,[100,200])
    display.blit(transform_big_boom,[100,300])

    pygame.display.flip()

pygame.init()

helper_load()
peremennaya_helper_load = helper_load()
middle_boom = pygame.image.load("pics/middle_boom.png")
big_boom = pygame.image.load("pics/big_boom.png")

transform_middle_boom = pygame.transform.scale(middle_boom,[24,24])
transform_big_boom = pygame.transform.scale(big_boom,[24,24])

fon = pygame.image.load("pics/fon.png")
sound_off = pygame.image.load("pics/off_sound.png")

transform_fon = pygame.transform.scale(fon, [1700, 1000])
transform_sound_off = pygame.transform.scale(sound_off, [70,70])

font = pygame.font.SysFont("arial", 20, True)

display = pygame.display.set_mode([1700, 1000])
