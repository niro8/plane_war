#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   plane_war.py
@Time    :   2023/09/18 08:32:25
@Author  :   Xiang Shuyue
@Version :   3.7
@Contact :   xiangshuyue@outlook.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

import pygame
import configparser
from interface import Background

config = configparser.ConfigParser()
config.read('game.ini')

width = config.getint('Settings', 'width')
height = config.getint('Settings', 'height')
caption = config.get('Settings', 'caption')
volume = config.getfloat('Settings', 'volume')
fps = config.getint('Settings', 'fps')


pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(caption)

# TEST = pygame.USEREVENT + 1
# pygame.time.set_timer(TEST, 2000)

# 背景音乐
# pygame.mixer.music.load('sound/game_music.ogg')
# pygame.mixer.music.set_volume(volume)
# pygame.mixer.music.play(-1)

# 背景组
bg1 = Background(0)
bg2 = Background(-height)
bg_group = pygame.sprite.Group(bg1, bg2)

while True:
    clock.tick(fps)
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # if event.type == TEST:
        #     print('Test Event')
    bg_group.update(screen)
    pygame.display.flip()
    