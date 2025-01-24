import random, pygame, time


def made_stone(x_stone, y_stone):
    stone_slovar = {"coord": pygame.Rect(x_stone, y_stone, 50, 50), "speed_x": random.randint(-3, 3),
                    "speed_y": random.randint(2, 3),
                    "angle": random.randint(0, 360), "coord_draw": [x_stone, y_stone]}

    stone_slovar["coord_float"] = [x_stone,y_stone]

    stone_slovar["spin"] = pygame.transform.rotate(transform_stone, stone_slovar["angle"])
    size_stone = stone_slovar["spin"].get_size()
    stone_slovar["center"] = [stone_slovar["coord"].x + size_stone[0] / 2, stone_slovar["coord"].y + size_stone[1] / 2]

    while stone_slovar["speed_x"] == 0 or stone_slovar["speed_x"] == -1 or stone_slovar["speed_x"] == 1:
        stone_slovar["speed_x"] = random.randint(-3, 3)

    return stone_slovar


def polet_stone(stone):
    size_stone_static = transform_stone.get_size()
    stone["coord_float"][0] += stone["speed_x"] / 3.5
    stone["coord_float"][1] += stone["speed_y"] / 2.5
    stone["coord"].x = stone["coord_float"][0]
    stone["coord"].y = stone["coord_float"][1]

    stone["center"] = [stone["coord"].x + size_stone_static[0] / 2, stone["coord"].y + size_stone_static[1] / 2]
    stone["spin"] = pygame.transform.rotate(transform_stone, stone["angle"])
    stone["angle"] += 2.5

    size_stone = stone["spin"].get_size()
    center_spin_stone = [stone["coord"].x + size_stone[0] / 2, stone["coord"].y + size_stone[1] / 2]
    center_spin_stone[0] -= stone["center"][0]  # center_spin_stone - разница между крутившемся и обычными центрами по х
    center_spin_stone[1] -= stone["center"][1]  # center_spin_stone - разница между крутившемся и обычными центрами по y

    stone["coord_draw"][0] = stone["coord"].x - center_spin_stone[0]
    stone["coord_draw"][1] = stone["coord"].y - center_spin_stone[1]


def paint(stone, display: pygame.Surface):
    display.blit(stone["spin"], stone["coord_draw"])
    size_stone = stone["spin"].get_size()

    # pygame.draw.circle(display, [255, 0, 0],
    #                    [stone["coord_draw"][0] + size_stone[0] / 2, stone["coord_draw"][1] + size_stone[1] / 2], 3)###ЦЕНТР РЕКТА КАМНЯ###
    # pygame.draw.rect(display, [255, 255, 255],
    #                  [stone["coord_draw"][0], stone["coord_draw"][1], size_stone[0], size_stone[1]], 3) ###РЕКТ КАМНЯ###


stone = pygame.image.load("pics/Meteorit.png")
transform_stone = pygame.transform.scale(stone, [50, 50])
