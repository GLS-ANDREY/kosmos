import time

import pygame, model, random, stone, bullet, hp_bar, sounds, points, samolet, image_helpers, gift_hp

def paint():
    global boom_tf
    display.fill([0, 0, 0])
    display.blit(fon, [0, 0])

    if sounds.sound_off_on == 0:
        display.blit(off_sound, [1630, 60])

    for infa_stone in model.all_stone:
        stone.paint(infa_stone, display, model.otladka)

    for infa_bullet in model.all_bullet:
        bullet.paint(infa_bullet, display, model.otladka)

    for infa_gift in model.all_gifts:
        gift_hp.paint(infa_gift, display, model.otladka)

    points.paint(display)

    hp_bar.paint(display)

    samolet.paint(display, model.otladka)

    if model.animation_boom_tf == True:
        model.animation_boom_tf = False
        boom_tf += 1
        if boom_tf == 4:
            boom_tf = 1
#TODO: Написать таймер в модели, а не в паинте
    display.blit(list_booms[boom_tf-1], [100, 100])

    pygame.display.flip()

pygame.init()

boom_tf = 1

small_boom = image_helpers.helper_load("pics/small_boom.png", 24, 24)
middle_boom = image_helpers.helper_load("pics/middle_boom.png", 24, 24)
big_boom = image_helpers.helper_load("pics/big_boom.png", 24, 24)
list_booms = [small_boom,middle_boom,big_boom]

off_sound = image_helpers.helper_load("pics/off_sound.png", 70, 70)
fon = image_helpers.helper_load("pics/fon.png", 1700, 1000)

font = pygame.font.SysFont("arial", 20, True)

display = pygame.display.set_mode([1700, 1000])
