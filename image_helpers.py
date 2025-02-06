import pygame

def to_grayscale(surface):
    width, height = surface.get_size()
    grayscale_surface = pygame.Surface((width, height),pygame.SRCALPHA)
    for y in range(height):
        for x in range(width):
            r, g, b, a = surface.get_at((x, y))
            # gray = int(0. * r + 0.65 * g + 0.25 * b)
            color = to_gold(r,g,b,0.6)
            grayscale_surface.set_at((x, y), color)
    return grayscale_surface

def to_gold(r, g, b, alpha=0.6):
    gold_r, gold_g, gold_b = 212, 175, 55
    new_r = int(r * (1 - alpha) + gold_r * alpha)
    new_g = int(g * (1 - alpha) + gold_g * alpha)
    new_b = int(b * (1 - alpha) + gold_b * alpha)
    return new_r, new_g, new_b

def poly_prosrathnost(surface:pygame.Surface,number):
    s2=surface.convert_alpha()
    s2.set_alpha(number)
    width, height = surface.get_size()
    grayscale_surface = pygame.Surface((width, height),pygame.SRCALPHA)
    grayscale_surface.blit(s2,[0,0])
    return grayscale_surface