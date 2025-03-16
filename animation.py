import pygame,time,random,messenger,os,image_helpers

# def animation():
#     global boom_tf
#     boom_tf += 1
#     if boom_tf == 4:
#         boom_tf = 1
#
image_number = 1
list_file = []
def animation_pics(display):#view
    folder_path = "pics/blue_open"

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        list_file.append(file_path)

    loaded_file = image_helpers.helper_load(list_file[image_number-1], 70, 100)
    display.blit(loaded_file,[500,500])

def animation():#model
    global image_number
    image_number += 1
    if image_number == 16:
        image_number = 1
