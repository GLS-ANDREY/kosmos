import pygame,time,random,messenger,os,image_helpers

image_number = 1
list_file = []

def made_animation(coord_x,coord_y,stop):
    slovar_animation = {"coord": [coord_x,coord_y], "stop": stop}
    return slovar_animation

def animation_pics(animation, display,folder_path):#view
    global list_file
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        list_file.append(file_path)
#Он берет 0 у портала и взрывы, далее в аниматион он становится 2 из за 1+1, потом 4, а у огня нету 4 элемента, а у портала есть
    loaded_file = image_helpers.helper_load(list_file[image_number-1], 70, 100)
    display.blit(loaded_file,animation["coord"])
    list_file = []

def animation(animation):#model
    global image_number
    image_number += 1
    if image_number == animation["stop"]:
        image_number = 1
