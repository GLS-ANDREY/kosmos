import pygame,time,random,messenger,os,image_helpers

def made_animation(coord_x,coord_y,stop,folder_path,size):
    slovar_animation = {"coord": [coord_x,coord_y], "stop": stop, "image_number": 0, "folder_path": folder_path, "size": size}
    return slovar_animation

def animation_pics(animation, display):#view
    list_file = []
    for file_name in os.listdir(animation["folder_path"]):
        file_path = os.path.join(animation["folder_path"], file_name)
        loaded_file = image_helpers.helper_load_procent(file_path, animation["size"],animation["size"])
        list_file.append(loaded_file)
        animation["pics"] = list_file

    display.blit(animation["pics"][animation["image_number"]],animation["coord"])
#TODO: Сделать чтобы не загружалось много картинок (см. консоль)
def animation(animation):#model
    animation["image_number"] += 1
    if animation["image_number"] == animation["stop"]:
        animation["image_number"] = 0
