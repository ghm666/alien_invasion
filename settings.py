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

        # ship 设置
        self.ship_speed_factor = 20
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 30
        self.fleet_drop_speed = 10
        # fleet_direction 为1表示向右移， -1表示向左移动
        self.fleet_direction = 1



