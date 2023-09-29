#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   player.py
@Time    :   2023/09/19 22:55:58
@Author  :   Xiang Shuyue
@Version :   3.7
@Contact :   xiangshuyue@outlook.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

import pygame
from config import Config

class HeroPlane(pygame.sprite.Sprite, Config):

    def __init__(self):
        super().__init__()
        Config.__init__(self)
        self.image = pygame.image.load('images/me1.png')
        self.image_other = pygame.image.load('images/me2.png')
        self.image_rect = self.image.get_rect()
        self.speed = 5
        self.image_rect.center = (self.x, self.y)
        self.bullet_type = 'normal' # 初始化的子弹是普通子弹

    def move(self, key):
        if key == pygame.K_UP and self.image_rect.top > 0:
            self.image_rect = self.image_rect.move(0, -self.speed)
        elif key == pygame.K_DOWN and self.image_rect.bottom < self.height-60:
            self.image_rect = self.image_rect.move(0, self.speed)
        elif key == pygame.K_LEFT and self.image_rect.left > 0:
            self.image_rect = self.image_rect.move(-self.speed, 0)
        elif key == pygame.K_RIGHT and self.image_rect.right < self.width:
            self.image_rect = self.image_rect.move(self.speed, 0)
        
    
    def update(self, screen, switch_flag):
        if switch_flag:
            screen.blit(self.image, self.image_rect)
        else:
            screen.blit(self.image_other, self.image_rect)

