import pygame, messenger
pygame.init()

sound_off_on = 0.2
#TODO: Сделать звук для вылетания камней sounds/unknown4.mp3 и сделать гладкую картинку мута
stone_break_sound = pygame.mixer.Sound("sounds/player is shot or the base (eagle) is blown up.mp3")
stone_break_sound.set_volume(0.02)

def sound(text,otpravitel,dop_infa):
    if text == "Пуля сбила камень":
        stone_break_sound.play()

messenger.add_me_to_chat(sound)
