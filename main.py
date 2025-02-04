import pygame, view, model, controller, time,sounds,bullet

while True:
    print(len(model.all_bullet))
    view.risovanie()
    controller.allsobitiya()
    time.sleep(1 / 10000)
