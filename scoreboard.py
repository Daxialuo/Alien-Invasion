# -*- coding: utf-8 -*-
"""
Created at 09 Jan 2019 00:32:18
Author : DaxiaLuo
"""

import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard():
    """显示得分信息的类"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 30)

        # 准备初始得分、最高得分、等级以及剩余飞船数的图像
        self.prep_images()

    def prep_images(self):
        """准备初始得分、最高得分、等级以及剩余飞船数的图像"""
        self.prep_score()
        self.prep_highest_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """将得分转换为一幅渲染的图像"""
        rounded_score = round(self.stats.score, 0)
        # print(rounded_score)
        score_str = "Score" + ": " + "{:,}".format(rounded_score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_highest_score(self):
        """将最高得分转换为渲染的图像"""
        highest_score = round(self.stats.highest_score, 0)
        highest_score_str = "Highest Score" + \
            ": " + "{:,}".format(highest_score)
        self.highest_score_image = self.font.render(
            highest_score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将最高得分放在屏幕顶部中央
        self.highest_score_rect = self.highest_score_image.get_rect()
        self.highest_score_rect.centerx = self.screen_rect.centerx
        self.highest_score_rect.top = self.score_rect.top

    def prep_level(self):
        """将等级转换为渲染的图像"""
        level_str = "Level" + ": " + str(self.stats.level)
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.ai_settings.bg_color)

        # 降等级显示在得分的下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """显示还剩下多少飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highest_score_image, self.highest_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # 绘制剩余飞船
        self.ships.draw(self.screen)
