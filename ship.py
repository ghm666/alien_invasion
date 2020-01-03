#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
# author: gaohuiming

import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """ 初始化飞船并设置其位置 """
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载图像并获取其外接距形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每一艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom  = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # move flag
        self.move_right = False
        self.move_left = False

    def update(self):
        """ 根据移动标志调整飞船的位置 """
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
        
        self.rect.centerx = self.center

    def blitme(self):
        """ 在指定位置绘制飞船 """
        self.screen.blit(self.image, self.rect)

