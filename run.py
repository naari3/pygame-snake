# -*- coding:utf-8 -*-

import pygame
from pygame.locals import *
import sys
import config

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 450
MASS = 25 # 1マスのおおきさ

keymap = {}

def quit():
    pygame.quit()       # Pygameの終了(画面閉じられる)
    sys.exit()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # WINDOW_WIDTH * WINDOW_HEIGHTの窓つくる
    pygame.display.set_caption("snake")
    font = pygame.font.Font(None, 25)

    while (True):
        screen.fill((0,0,0))        # 画面を黒色(#000000)に塗りつぶし
        pygame.draw.rect(screen, (255,255,255), Rect(0,0,WINDOW_WIDTH,25))
        pygame.draw.rect(screen, (255,255,255), Rect(50,50,MASS,MASS))
        text = font.render("TEST", True, (0,0,0))
        screen.blit(text, [5, 0])
        pygame.display.update()     # 画面を更新

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                quit()
            if event.type == KEYDOWN:
                keymap[event.scancode] = event.unicode
                print('keydown %s pressed' % event.unicode)
                if (event.key == K_ESCAPE):
                    os._exit(0)

            if event.type == KEYUP:
                print('keyup %s pressed' % keymap[event.scancode])

if __name__ == "__main__":
    main()
