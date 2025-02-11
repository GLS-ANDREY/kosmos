import pygame


def paint(display):
    text_point = font.render(zero, True, [255, 255, 255])
    display.blit(text_point, [1540, 5])


def plus_point():
    global point
    point += 1
    _rasschet()

def _rasschet():
    global zero
    kolvo_simvolov_point = len(str(point))
    kolvo_zero = 5 - kolvo_simvolov_point
    zero = "0" * kolvo_zero + str(point)

pygame.init()
font = pygame.font.SysFont("hooge0555", 50, False)

point = 0
_rasschet()