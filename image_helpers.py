import pygame


def to_gold_tone(surface):
    width, height = surface.get_size()
    gold_surface = pygame.Surface((width, height), pygame.SRCALPHA)

    for y in range(height):
        for x in range(width):
            r, g, b, a = surface.get_at((x, y))
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)  # Перевод в оттенки серого

            # Градиент золотого цвета
            gold_r = min(255, int(gray * 1.7) * 3)  # Усиливаем красный компонент
            gold_g = min(255, int(gray * 1.3) * 3)  # Усиливаем зеленый
            gold_b = min(255, int(gray * 0.0) * 3)  # Ослабляем синий (делает цвет теплым)

            gold_surface.set_at((x, y), (gold_r, gold_g, gold_b, a))  # Устанавливаем пиксель

    return gold_surface


def to_grayscale(surface):
    width, height = surface.get_size()
    grayscale_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    for y in range(height):
        for x in range(width):
            r, g, b, a = surface.get_at((x, y))
            # gray = int(0. * r + 0.65 * g + 0.25 * b)
            color = to_gold(r, g, b, 0.6)
            grayscale_surface.set_at((x, y), color)
    return grayscale_surface


def to_gold(r, g, b, alpha=0.6):
    gold_r, gold_g, gold_b = 212, 175, 55
    new_r = int(r * (1 - alpha) + gold_r * alpha)
    new_g = int(g * (1 - alpha) + gold_g * alpha)
    new_b = int(b * (1 - alpha) + gold_b * alpha)
    return new_r, new_g, new_b


def poly_prosrathnost(surface: pygame.Surface, number):
    s2 = surface.convert_alpha()
    s2.set_alpha(number)
    width, height = surface.get_size()
    grayscale_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    grayscale_surface.blit(s2, [0, 0])
    return grayscale_surface


def helper_load(file_name, size_x, size_y):
    kartinka = pygame.image.load(file_name)
    transform_kartinka = pygame.transform.scale(kartinka, [size_x, size_y])
    return transform_kartinka


def helper_load_procent(file_name, size_x_procent, size_y_procent):
    print(file_name)
    kartinka = pygame.image.load(file_name)
    transform_kartinka = pygame.transform.scale(kartinka, [kartinka.get_width()*(size_x_procent/100), kartinka.get_height()*(size_y_procent/100)])
    return transform_kartinka
