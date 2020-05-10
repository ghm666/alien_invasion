#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
# author: gaohuiming

class GameStats():
    """ 跟踪游戏的统计信息 """
    
    def __init__(self, ai_settings):
        """ 初始化统计信息 """
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏刚启动时处于活动状态
        self.game_activate = True
        
    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_limit