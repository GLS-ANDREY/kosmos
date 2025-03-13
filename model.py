import pygame, random, bullet, messenger, points, gift_hp


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

def stone_popal_v_samolet(text, otpravitel, dop_infa):
    if text == "Камень попал по самолету":
        all_stone.remove(otpravitel)



messenger.add_me_to_chat(sbivanie_stone)
messenger.add_me_to_chat(bullet_za_granicey)
messenger.add_me_to_chat(stone_za_granicey)
messenger.add_me_to_chat(sbor_gift)
messenger.add_me_to_chat(stone_popal_v_samolet)

animation_boom_tf = False

all_gifts = []
all_bullet = []
all_stone = []
otladka = False