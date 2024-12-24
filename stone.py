import random, pygame

def made_stone(x_stone, y_stone):
    stone_slovar = {"coord": [x_stone, y_stone], "speed_x": random.randint(-3, 3), "speed_y": random.randint(2, 3),
                    "angle": random.randint(0, 360), "center_x": 10, "center_y": 10}
    stone_slovar["rotate"] = pygame.transform.rotate(transform_stone, stone_slovar["angle"])

    while stone_slovar["speed_x"] == 0 or stone_slovar["speed_x"] == -1 or stone_slovar["speed_x"] == 1:
        stone_slovar["speed_x"] = random.randint(-3, 3)

    return stone_slovar


def polet_stone(stone):
    # stone["coord"][0] += stone["speed_x"]
    # stone["coord"][1] += stone["speed_y"]
    stone["rotate"] = pygame.transform.rotate(transform_stone, stone["angle"])
    stone["angle"] += 1


def paint(stone, display: pygame.Surface):
    display.blit(stone["rotate"], stone["coord"])
    size_stone = stone["rotate"].get_size()
    pygame.draw.circle(display,[255,0,0],[stone["coord"][0]+size_stone[0]/2,stone["coord"][1]+size_stone[1]/2],3)
    pygame.draw.rect(display,[255,255,255],[stone["coord"][0],stone["coord"][1],size_stone[0],size_stone[1]],3)


stone = pygame.image.load("pics/Meteorit.png")
transform_stone = pygame.transform.scale(stone, [50, 50])
