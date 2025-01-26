import pygame, messenger

rect_hp_bar = pygame.Rect(0,0,300,100)

def paint(display):
    pygame.draw.rect(display, [17, 255, 21], rect_hp_bar)
    pygame.draw.rect(display, [255, 255, 255], rect_hp_bar,3)



def hp(text,otpravitel,dop_infa):
    pass





messenger.add_me_to_chat(hp)