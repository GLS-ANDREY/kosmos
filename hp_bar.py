import pygame, messenger, image_helpers, random


def paint(display: pygame.Surface):
    display.blit(transform_hp_bar_surface, [0, 0])

    real_width_red_bar = rect_red_hp_bar.width
    coord_x_risovnie_red_bar = red_hp_bar.get_width() - real_width_red_bar

    transform_hp_red_surface = pygame.transform.scale(red_hp_bar, [rect_red_hp_bar.width, rect_red_hp_bar.height])
    display.blit(transform_hp_red_surface, [coord_x_risovnie_red_bar + 86, rect_red_hp_bar.y])
    if creative_mode == True:
        display.blit(gold_hp_bar, [rect_red_hp_bar.x, rect_red_hp_bar.y])


def heal_hp():
    global int_hp
    int_hp -= 20
    _ustanovi_hp()


def creative_mode_on():
    global creative_mode
    creative_mode = not creative_mode
    _ustanovi_hp()


def _hp(text, otpravitel, dop_infa):
    global int_hp

    if text == "Камень попал по самолету":
        helper_hp(-20)

    if text == "Камень вылетел за экран":
        helper_hp(-20)

    if text == "Самолет собрал подарок":
        helper_hp(20)


def helper_hp(add_hp):
    global int_hp
    if not creative_mode:
        int_hp += add_hp
        _ustanovi_hp()


def _ustanovi_hp():
    global int_hp

    if creative_mode == True:
        int_hp = 100

    rect_red_hp_bar.width = red_hp_bar.get_width()
    new_hp = (100 - int_hp) * rect_red_hp_bar.width / 100
    rect_red_hp_bar.width = new_hp

    if int_hp > 100:
        int_hp = 100
        rect_red_hp_bar.width = 0

    if int_hp <= 0:
        int_hp = 0
        rect_red_hp_bar.width = 243


rect_red_hp_bar = pygame.Rect(86, 15, 0, 46)
creative_mode = False
int_hp = 100

red_hp_bar = pygame.image.load("pics/red_hp.png")
# gold_hp_bar = pygame.image.load("pics/gold_hp.png")
hp_bar_surface = pygame.image.load("pics/hp_bar.png")
transform_hp_bar_surface = pygame.transform.scale(hp_bar_surface,
                                                  [hp_bar_surface.get_width() / 3, hp_bar_surface.get_height() / 3])
import image_helpers

gold_hp_bar = image_helpers.to_gold_tone(red_hp_bar)

messenger.add_me_to_chat(_hp)
