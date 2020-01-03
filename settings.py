#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
# author: gaohuiming

class Settings():
    """
    存储外星人入侵所有设置的类
    """

    def __init__(self):
        """初始化游戏的设置"""

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        self.ship_speed_factor = 10
