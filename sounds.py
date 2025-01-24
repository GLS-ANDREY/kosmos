import pygame, messenger
stone_break_sound = pygame.mixer.Sound("sounds/shot against a concrete barrier.mp3")

#TODO: Сделать кнопку для отключения звуков
def sound(text,otpravitel,dop_infa):
    stone_break_sound.play()

messenger.add_me_to_chat(sound)
