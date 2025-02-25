import pygame,random,samolet,messenger

def made_gift():
    x_gift = random.randint(50,1650)
    gift_slovar = {"coord": pygame.Rect(x_gift, -70, 42, 42), "speed_y": 3}
    return gift_slovar

def paint(gift,display:pygame.Surface):
    display.blit(transform_parashut,[gift["coord"].x-25,gift["coord"].y-75])
    display.blit(transform_gift,gift["coord"])
    # pygame.draw.rect(display,[255,255,255],gift["coord"],2)

def collect_gift(gift):
    sbor_podarka = gift["coord"].collidelist(samolet.samolet_slovar["hit_rect"])
    if sbor_podarka != -1:
        messenger.send_message("Самолет собрал подарок",gift)

def polet_gifta(gift):
    gift["coord"].y += gift["speed_y"]
    gift["speed_y"] -= 0.003
    if gift["coord"].y >= 965:
        gift["speed_y"] -= 10
    if gift["speed_y"] > 0:
        collect_gift(gift)


gift = pygame.image.load("pics/Chest.png")
parashut = pygame.image.load("pics/parashut.png")
transform_gift = pygame.transform.scale(gift,[40,40])
transform_parashut = pygame.transform.scale(parashut,[90,90])