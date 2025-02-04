import pygame, messenger,image_helpers,random

rect_red_hp_bar = pygame.Rect(86,15,0,46)

def paint(display:pygame.Surface):
    display.blit(transform_hp_bar_surface,[0,0])

    real_width_red_bar = rect_red_hp_bar.width
    coord_x_risovnie_red_bar = red_hp_bar.get_width() - real_width_red_bar

    transform_hp_red_surface = pygame.transform.scale(red_hp_bar, [rect_red_hp_bar.width, rect_red_hp_bar.height])
    display.blit(transform_hp_red_surface,[coord_x_risovnie_red_bar+86,rect_red_hp_bar.y])

def heal_hp():
    global int_hp
    int_hp += 20
    ustanovi_hp()

def hp(text,otpravitel,dop_infa):
    global int_hp
    int_hp = int_hp-20
    ustanovi_hp()

def ustanovi_hp():
    global int_hp
    rect_red_hp_bar.width = red_hp_bar.get_width()
    new_hp = (100-int_hp)*rect_red_hp_bar.width/100
    rect_red_hp_bar.width = new_hp
    if int_hp > 100:
        int_hp = 100
        rect_red_hp_bar.width = 0
    if int_hp <= 0:
        int_hp = 0
        rect_red_hp_bar.width = 243



int_hp = 100

red_hp_bar = pygame.image.load("pics/red_hp.png")
hp_bar_surface = pygame.image.load("pics/hp_bar.png")
transform_hp_bar_surface = pygame.transform.scale(hp_bar_surface, [hp_bar_surface.get_width()/3, hp_bar_surface.get_height()/3])

messenger.add_me_to_chat(hp)