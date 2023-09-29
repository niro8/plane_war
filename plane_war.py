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
from player import HeroPlane
from bullet import Bullet


config = configparser.ConfigParser()
config.read('game.ini', encoding='utf-8')

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

# 创建玩家飞机
heroplane = HeroPlane()

# 标识玩家飞机图像切换事件
IMAGE_FLAG = pygame.USEREVENT + 1
pygame.time.set_timer(IMAGE_FLAG, 100)
switch_flag = True

# 发射子弹事件
FIRE = pygame.USEREVENT + 2
pygame.time.set_timer(FIRE, 200)

bullets = pygame.sprite.Group()

while True:
    clock.tick(fps)
    key_pressed = pygame.key.get_pressed()
    for key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
        if key_pressed[key]:
            heroplane.move(key)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == IMAGE_FLAG:
            if switch_flag:
                switch_flag = False
            else:
                switch_flag = True
        if event.type == FIRE:
            bullet = Bullet(heroplane.bullet_type, heroplane.image_rect.midtop)
            bullets.add(bullet)
    bg_group.update(screen)
    heroplane.update(screen, switch_flag)
    bullets.update(screen, bullets)
    pygame.display.update()
