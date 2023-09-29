#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   bullets.py
@Time    :   2023/09/21 23:23:14
@Author  :   Xiang Shuyue
@Version :   3.7
@Contact :   xiangshuyue@outlook.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

import pygame
from PIL import Image

class Bullet(pygame.sprite.Sprite):

    def __init__(self, bullet_type, pos):
        super().__init__()
        if bullet_type == 'normal':
            self.image = pygame.image.load('images/bullet1.png').convert_alpha()
        else:
            self.image = pygame.image.load('images/bullet2.png')
        self.image_rect =  self.image.get_rect()
        self.image_rect.midbottom = pos
        self.speed = 7
    
    def update(self, screen, bullets):
        if self.image_rect.y > 0:
            self.image_rect.y -= self.speed
            screen.blit(self.image, self.image_rect)
        else:
            bullets.remove(self)
        