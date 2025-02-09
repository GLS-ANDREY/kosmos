import pygame

def paint(display):
    text_point = font.render(point, True, [255,255,255])
    display.blit(text_point,[100,100])






#TODO: нужно создать новую строку с нужным нам кол-вом нулей: a = "0"*3
font = pygame.font.SysFont("arial", 40, True)
point = "1"
zero = "00000"
kolvo_simvolov_point = len(point)
