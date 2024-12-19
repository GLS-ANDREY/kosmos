import random, pygame

#TODO: что бы нарисовался другой камень нужно изменить картинку камня "rotate"

def made_stone(x_stone, y_stone):
    stone_slovar = {"coord": [x_stone, y_stone], "speed_x": random.randint(-3, 3), "speed_y": random.randint(2, 3),
                    "angle": random.randint(0,360),"rotate": pygame.transform.rotate(transform_stone,random.randint(0,360))}
    while stone_slovar["speed_x"] == 0 or stone_slovar["speed_x"] == -1 or stone_slovar["speed_x"] == 1:
        stone_slovar["speed_x"] = random.randint(-3, 3)
    return stone_slovar

def polet_stone(stone):
    stone["coord"][0] += stone["speed_x"]/10
    stone["coord"][1] += stone["speed_y"]/10

def paint(stone, display: pygame.Surface):
    global rotate_stone
    display.blit(stone["rotate"], stone["coord"])

stone = pygame.image.load("pics/Meteorit.png")
transform_stone = pygame.transform.scale(stone, [50, 50])
