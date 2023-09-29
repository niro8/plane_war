#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   interface.py
@Time    :   2023/09/18 23:21:42
@Author  :   Xiang Shuyue
@Version :   3.7
@Contact :   xiangshuyue@outlook.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

import pygame


class Background(pygame.sprite.Sprite):

    def __init__(self, y=0):
        super().__init__()
        self.image = pygame.image.load('images/background.png')
        self.image_rect = self.image.get_rect()
        self.image_rect.y = y
        self.speed = 1
    
    def update(self, screen):
        if self.image_rect.y > screen.get_rect().height:
            self.image_rect.y = -screen.get_rect().height
        else:
            self.image_rect.y += self.speed
        screen.blit(self.image, self.image_rect)

