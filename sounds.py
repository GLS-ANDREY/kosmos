import pygame, messenger
pygame.init()

sound_off_on = 0.2
stone_break_sound = pygame.mixer.Sound("sounds/player is shot or the base (eagle) is blown up.mp3")
stone_break_sound.set_volume(0.02)
stone_bye_sound = pygame.mixer.Sound("sounds/unknown4.mp3")
stone_bye_sound.set_volume(0.02)

def sound(text,otpravitel,dop_infa):
    if text == "Пуля сбила камень":
        stone_break_sound.play()
    if text == "Камень вылетел за экран":
        stone_bye_sound.play()

messenger.add_me_to_chat(sound)
