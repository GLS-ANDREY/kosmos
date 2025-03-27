import pygame, random, bullet, messenger, points, gift_hp, animation

def sbivanie_stone(text, otpravitel, dop_infa):
    if text == "Пуля сбила камень":
        all_bullet.remove(otpravitel)
        points.plus_point()

def bullet_za_granicey(text, otpravitel, dop_infa):
    if text == "Пуля вышла за экран":
        all_bullet.remove(otpravitel)

def stone_za_granicey(text, otpravitel, dop_infa):
    if text == "Камень вылетел за экран":
        all_stone.remove(otpravitel)

def sbor_gift(text, otpravitel, dop_infa):
    if text == "Самолет собрал подарок":
        all_gifts.remove(otpravitel)

def stone_popal_v_samolet(text=None, otpravitel=None, dop_infa=None):
    global paint_or_not_paint, animation_one
    if text == "Камень попал по самолету":
        all_stone.remove(otpravitel)
        object_slovar_animation = animation.made_animation(dop_infa.x, dop_infa.y, "pics/fire", 200)
        animation_one = object_slovar_animation
        paint_or_not_paint = True


messenger.add_me_to_chat(sbivanie_stone)
messenger.add_me_to_chat(bullet_za_granicey)
messenger.add_me_to_chat(stone_za_granicey)
messenger.add_me_to_chat(sbor_gift)
messenger.add_me_to_chat(stone_popal_v_samolet)

paint_or_not_paint = False

all_gifts = []
all_bullet = []
all_stone = []

animation_one = None

# object_slovar_animation = animation.made_animation(500,500, "pics/blue_open",30)
# animation_one2 = object_slovar_animation

otladka = False