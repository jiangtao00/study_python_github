#!/usr/bin/env python
# -*-coding:utf-8 -*-
# __author__ = "john"
# Date: 2018/11/

from python_project.Airplane.plane_sprites import *
import pygame

pygame.init()

# create the window 480 * 700
screen = pygame.display.set_mode((400, 700))

# create the background of the game
# loading the picture
bg = pygame.image.load("./images/background.png")
# use "blit" to create picture
screen.blit(bg, (0, 0))

# # use update to update the screen
# pygame.display.update()

# the hero of airplane
hero = pygame.image.load("./images/hero.gif")
screen.blit(hero, (140, 500))

# we can use update just one time when we have created all object about airplane
pygame.display.update()

# create an object of clock
clock = pygame.time.Clock()

# 1. 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 100, 124)


# 创建敌机的精灵
enemy = GameSprite("./images/enemy0.png")
enemy1 = GameSprite("./images/enemy0.png", 2)
# 创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)


# 游戏循环 -> 意味着游戏的正式开始  上方是游戏的初始化
while True:

    # 1.specifies the frequency of code execution inside the loop body
    clock.tick(60)

    # capture action
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("game is over")
            # uninstall all module
            pygame.quit()
            # exit
            exit()

    # 2. change the location of the airplane
    hero_rect.y -= 1
    # 3. assert the location of the airplane
    if hero_rect.y <= -124:
        hero_rect.y = 700
    # 3. use blit ways to create picture
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法
    # update - 让组中所有精灵更新位置
    enemy_group.update()
    # draw - 在screen上绘制所有的精灵组
    enemy_group.draw(screen)


    # 4. use update ways to update screen
    pygame.display.update()

pygame.quit()