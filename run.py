# -*- coding:utf-8 -*-

import pygame
from pygame.locals import *
import sys
import random

MASS_SIZE = 100 # １マスのおおきさ

REWARD = 1 # 果物１つにつき伸びる体の数
fps = 60 # Frame Per Second １秒間に何フレームか
fpa = 10 # Frame Per Advance 何フレームで１つ進むか

w, h = 5, 5 # マップの広さ
# x, y =

MASS_WIDTH = w + 2
MASS_HEIGHT = h + 2

maps = [[1 if i == 0 or i == MASS_HEIGHT-1 else 0 for i in range(MASS_HEIGHT)] for j in range(MASS_WIDTH)]
wall = [1 for i in range(MASS_HEIGHT)]
maps[0] = wall
maps[MASS_WIDTH-1] = wall
# 0:空間 1:壁 2:ヘビ 3:りんご

SCREEN_WIDTH = (MASS_WIDTH-2) * MASS_SIZE
SCREEN_HEIGHT = (MASS_HEIGHT-2) * MASS_SIZE

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)

snake_direction = 0 # 0:R 1:D 2:L 3: U
class Snake(object):
    def __init__(self, body, maps, screen, direction=0, pos=(0,1)):
        self.body = body
        self.direction = direction
        self.maps = maps
        self.x = pos[0]
        self.y = pos[1]
        self.status = 0 # 0:normal, 1:rewarding, 2:death
        self.score = 0
        self.tick = 0
        self.now_direction = direction
        self.screen = screen

    def update(self):
        if self.tick == 0:
            self.check(self.x, self.y)
            self.advance()
            self.now_direction = self.direction
            draw_game(self.screen)
            # for m in self.maps:
            #     print(m)
            print(self.score)

        if self.tick != fpa:
            self.tick += 1
        else:
            self.tick = 0

    def advance(self):
        if self.direction == 0:
            self.maps[self.x+1][self.y] = 2
            self.adv_post_process()
            self.x += 1
        elif self.direction == 1:
            self.maps[self.x][self.y+1] = 2
            self.adv_post_process()
            self.y += 1
        elif self.direction == 2:
            self.maps[self.x-1][self.y] = 2
            self.adv_post_process()
            self.x -= 1
        elif self.direction == 3:
            self.maps[self.x][self.y-1] = 2
            self.adv_post_process()
            self.y -= 1

    def adv_post_process(self):
        self.maps[self.body[-1][0]][self.body[-1][1]] = 0
        self.body.insert(0, (self.x, self.y))
        if self.status <= 0:
            self.body.pop()
        if self.status != 0:
            self.status -= 1

    def check(self, x, y):
        if self.direction == 0:
            checking = self.maps[x+1][y]
        elif self.direction == 1:
            checking = self.maps[x][y+1]
        elif self.direction == 2:
            checking = self.maps[x-1][y]
        elif self.direction == 3:
            checking = self.maps[x][y-1]

        if checking == 1 or checking == 2:
            self.death()
        elif checking == 3:
            self.reward()
            appleGenerate()

    def death(self):
        quit()

    def reward(self):
        self.status = REWARD
        self.score += 100

def appleGenerate():
    while True:
        x, y = random.randint(1,MASS_WIDTH-1), random.randint(1,MASS_HEIGHT-1)
        if maps[x][y] == 0:
            maps[x][y] = 3
            break


def draw_box(screen, color, mapsx, mapsy):
    x, y = (mapsx-1) * MASS_SIZE, (mapsy-1) * MASS_SIZE
    pygame.draw.rect(screen, color, Rect(x, y, MASS_SIZE, MASS_SIZE))

def draw_game(screen):
    for x in range(MASS_WIDTH):
        for y in range(MASS_HEIGHT):
            if maps[x][y] == 0:
                draw_box(screen, BLACK, x, y)
            elif maps[x][y] == 1:
                draw_box(screen, WHITE, x, y)
            elif maps[x][y] == 2:
                draw_box(screen, GREEN, x, y)
            elif maps[x][y] == 3:
                draw_box(screen, RED, x, y)

def game_init(surface):
    maps[x][y] = 2

def quit():
    pygame.quit()       # Pygameの終了(画面閉じられる)
    sys.exit()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # WINDOW_WIDTH * WINDOW_HEIGHTの窓つくる
    pygame.display.set_caption("snake")
    font = pygame.font.Font(None, 25)

    appleGenerate()

    snake = Snake([(5,5)], maps, screen)
    clock = pygame.time.Clock()
    screen.fill(BLACK)

    while (True):
        clock.tick(fps)
        # text = font.render("TEST", True, BLACK)
        # screen.blit(text, [5, 0])
        snake.update()

        pygame.display.update()     # 画面を更新

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                quit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT and snake.now_direction != 2:
                    snake.direction = 0

                if event.key == K_DOWN and snake.now_direction != 3:
                    snake.direction = 1

                if event.key == K_LEFT and snake.now_direction != 0:
                    snake.direction = 2

                if event.key == K_UP and snake.now_direction != 1:
                    snake.direction = 3

                if (event.key == K_ESCAPE):
                    quit()

if __name__ == "__main__":
    main()
