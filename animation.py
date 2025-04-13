import pygame, time, random, messenger, os, image_helpers


def made_animation(coord_x, coord_y, folder_path, size, life_time):
    fire_potux = pygame.event.custom_type()
    pygame.time.set_timer(fire_potux, 2000)
    slovar_animation = {"coord": [coord_x, coord_y], "image_number": 0, "folder_path": folder_path, "size": size,
                        "life_time": life_time, "active": True, "id_timer": fire_potux}

    list_file = []
    for file_name in os.listdir(slovar_animation["folder_path"]):
        file_path = os.path.join(slovar_animation["folder_path"], file_name)
        loaded_file = image_helpers.helper_load_procent(file_path, slovar_animation["size"], slovar_animation["size"])
        list_file.append(loaded_file)
    slovar_animation["pics"] = list_file

    return slovar_animation

def controller(animation, events):
    for a in events:
        if a.type == animation["id_timer"]:
            animation["active"] = False
#TODO: Нужно сделать огонь на самолете, нужно сделать много огней на всю программу, сделать самолет помедленнее, сделать что бы он двигался более короткими шагами, но чаще

def animation_pics(animation, display):  # view
    if animation["active"] == True:
        display.blit(animation["pics"][animation["image_number"]], animation["coord"])


def animation(animation):  # model
    animation["image_number"] += 1
    stop_pics = len(animation["pics"])
    if animation["image_number"] == stop_pics:
        animation["image_number"] = 0
