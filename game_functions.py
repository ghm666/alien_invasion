#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
# author: gaohuiming

import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ 响应按下 """
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """ 如果还没到达限制，就发射一颗子弹 """
    # 创建一颗子弹，将其加入到编组bullets
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """ 响应松开 """
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False

def check_events(ai_settings, screen, ship, bullets):
    """ 响应按键和鼠标事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, alien, bullets):
    """ 更新屏幕上的图像，并切换到新屏幕 """

    # 每次循环时都重新绘制屏幕
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    alien.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    """ 更新子弹的位置，并删除已消失的子弹 """
    
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))