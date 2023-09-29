#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   config.py
@Time    :   2023/09/19 23:08:56
@Author  :   Xiang Shuyue
@Version :   3.7
@Contact :   xiangshuyue@outlook.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

import configparser

class Config():

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('game.ini')
        self.width = self.config.getint('Settings', 'width')
        self.height = self.config.getint('Settings', 'height')
        self.caption = self.config.get('Settings', 'caption')
        self.volume = self.config.getfloat('Settings', 'volume')
        self.fps = self.config.getint('Settings', 'fps')

        self.x = self.config.getint('Player', 'x')
        self.y = self.config.getint('Player', 'y')
