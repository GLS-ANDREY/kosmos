import pygame, messenger,image_helpers,random

rect_red_hp_bar = pygame.Rect(86,15,0,46)

def paint(display:pygame.Surface):
    display.blit(transform_hp_bar_surface,[0,0])

    transform_hp_red_surface = pygame.transform.scale(red_hp_bar, [rect_red_hp_bar.width, rect_red_hp_bar.height])
    display.blit(transform_hp_red_surface,[86,15])

#TODO: Сделать что бы красное заходило с лево, а не с право, сделать уменьшение хп когда камень достигает пола (уменьшение хп на 20)
def hp(text,otpravitel,dop_infa):
    int_hp = random.randint(1, 100)
    ustanovi_hp(int_hp)


def ustanovi_hp(int_hp):
    rect_red_hp_bar.width = red_hp_bar.get_width()
    new_hp = (100-int_hp)*rect_red_hp_bar.width/100
    rect_red_hp_bar.width = new_hp



red_hp_bar = pygame.image.load("pics/red_hp.png")

hp_bar_surface = pygame.image.load("pics/hp_bar.png")
transform_hp_bar_surface = pygame.transform.scale(hp_bar_surface, [hp_bar_surface.get_width()/3, hp_bar_surface.get_height()/3])


messenger.add_me_to_chat(hp)