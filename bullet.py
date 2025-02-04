import pygame,messenger

def made_bullet(x_bullet, y_bullet):
    return {"coord": pygame.Rect(x_bullet, y_bullet, 6, 21)}

def paint(bullet, display: pygame.Surface,stone=None):
    display.blit(transform_bullet, bullet["coord"])
    # pygame.draw.rect(display, [255,255,255],[bullet["coord"][0],bullet["coord"][1],6,21],1) ###РЕКТ ПУЛИ###

def del_stone(bullet, stone_list):
    for collide_stone in stone_list:
        collide_t_or_f = bullet["coord"].colliderect(collide_stone["coord"])
        if collide_t_or_f == True:
            stone_list.remove(collide_stone)
            messenger.send_message("Пуля сбила камень",bullet)
#TODO: Сейчас при вылетании пули за экран, она удаляется и создается впечатление что мы сбили камень, нужно что бы она просто исчезала
def polet_pul(bullet, stone_list):
    bullet["coord"].y -= 5
    del_stone(bullet, stone_list)
    del_bullet(bullet)

def del_bullet(bullet):
    if bullet["coord"].y <= -15:
        messenger.send_message("Пуля вышла за экран", bullet)


bullet = pygame.image.load("pics/bullet.png")
transform_bullet = pygame.transform.scale(bullet, [6, 21])
