# -*- coding: utf-8 -*-
"""
Created at 07 Jan 2019 22:45:34
Author : DaxiaLuo
"""


class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始统计上信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏刚开始启动时处于非激活状态
        self.game_active = False

        # 读取历史最高得分
        with open('/home/luojuntao/Documents/LearningPython/alien_invasion/datas/highest_score.txt', 'r') as f:
            self.highest_score = int(f.read())

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
