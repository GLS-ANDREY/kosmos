import pygame, model, random, bullet, stone, gift_hp,hp_bar,samolet,sounds,points,animation

pygame.key.set_repeat(10)

# dvizhenie_puli = pygame.event.custom_type()
# pygame.time.set_timer(dvizhenie_puli, 10)
#
# dvizhenie_gift = pygame.event.custom_type()
# pygame.time.set_timer(dvizhenie_gift, 10)
#
# dvizhenie_stone = pygame.event.custom_type()
# pygame.time.set_timer(dvizhenie_stone, 10)

animation_timer = pygame.event.custom_type()
pygame.time.set_timer(animation_timer, 100)

dvizhenie_puli_stone_gift = pygame.event.custom_type()
pygame.time.set_timer(dvizhenie_puli_stone_gift, 10)

spawn_stone = pygame.event.custom_type()
pygame.time.set_timer(spawn_stone, 3000)

spawn_gift = pygame.event.custom_type()
pygame.time.set_timer(spawn_gift, 10000)


def allsobitiya():
    s = pygame.event.get()

    for a in s:
        if a.type == pygame.QUIT:
            exit()

        if a.type == animation_timer and type(model.animation_one) == dict:
            animation.animation(model.animation_one)
            # animation.animation(model.animation_one2)

        if a.type == spawn_gift:
            gift = gift_hp.made_gift()
            model.all_gifts.append(gift)

        if a.type == pygame.KEYUP and a.key == pygame.K_TAB:
            model.otladka = not model.otladka

        if a.type == dvizhenie_puli_stone_gift:
            for infa_gift in model.all_gifts:
                gift_hp.polet_gifta(infa_gift)

        if a.type == pygame.KEYUP and a.key == pygame.K_y:
            hp_bar.heal_hp()

        if a.type == pygame.KEYUP and (a.key == pygame.K_g or a.key == pygame.K_c):
            hp_bar.creative_mode_on()

        if a.type == spawn_stone:
            stone_slovar = stone.made_stone(random.randint(600, 900), -50)
            model.all_stone.append(stone_slovar)

        if a.type == dvizhenie_puli_stone_gift:
            for infa_bullet in model.all_bullet:
                bullet.polet_pul(infa_bullet, model.all_stone)

        if a.type == dvizhenie_puli_stone_gift:
            for infa_stone in model.all_stone:
                stone.polet_stone(infa_stone, samolet.samolet_slovar)

        if a.type == pygame.KEYUP and a.key == pygame.K_m:
            sounds.sound_off_on = 0.2 if sounds.sound_off_on == 0 else 0
            sounds.stone_break_sound.set_volume(sounds.sound_off_on)
            sounds.stone_bye_sound.set_volume(sounds.sound_off_on)

        if a.type == pygame.MOUSEBUTTONDOWN and (a.button == pygame.BUTTON_RIGHT or a.button == pygame.BUTTON_LEFT):
            if a.button == pygame.BUTTON_RIGHT:
                button = "right"
            else:
                button = "left"
            bs = samolet.strelba(button)
            model.all_bullet.append(bs)

        if a.type == pygame.KEYDOWN and a.key == pygame.K_d:
            samolet.dvizhenie_vpravo()
            stone.stone_popal_po_samoletu(model.all_stone, samolet.samolet_slovar)
        # TODO: Сделать чтобы проверка пересечения камня и самолета происходила при движении и камня, и самолета, сделать это в этом ифе и похожих на него, в строке выше сейчас указаны модули, нужно что бы были словари

        if a.type == pygame.KEYDOWN and a.key == pygame.K_a:
            samolet.dvizhenie_vlevo()

        if a.type == pygame.KEYDOWN and a.key == pygame.K_s:
            samolet.dvizhenie_vniz()

        if a.type == pygame.KEYDOWN and a.key == pygame.K_w:
            samolet.dvizhenie_vverx()

