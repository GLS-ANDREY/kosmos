import pygame, messenger,image_helpers

rect_hp_bar = pygame.Rect(0,0,300,100)

def paint(display:pygame.Surface):
    display.blit(transform_hp_bar_surface,[0,0])
    delitel_red_hp_width = 2
    transform_hp_red_surface = pygame.transform.scale(red_hp_bar, [red_hp_bar.get_width()/delitel_red_hp_width, red_hp_bar.get_height()])
    display.blit(transform_hp_red_surface,[86,15])



def hp(text,otpravitel,dop_infa):
    pass


def ustanovi_hp(int_hp):
    300/50=6
    6/2=3
    3*50=150



red_hp_bar = pygame.image.load("pics/red_hp.png")

hp_bar_surface = pygame.image.load("pics/hp_bar.png")
transform_hp_bar_surface = pygame.transform.scale(hp_bar_surface, [hp_bar_surface.get_width()/3, hp_bar_surface.get_height()/3])


messenger.add_me_to_chat(hp)