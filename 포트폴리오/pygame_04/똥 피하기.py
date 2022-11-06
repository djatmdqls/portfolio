from math import e
from random import random
from re import T
import pygame
import random

pygame.init()

hta = 3
aa = 0
bb = 0
세로 = 640
가로 = 480
화면 = pygame.display.set_mode((가로, 세로))
폰트 = pygame.font.SysFont("hy얕은샘물m", 30, True)
실패 = 폰트.render(f"실패", False, (0, 0, 0))
성공 = 폰트.render(f"성공", False, (0, 0, 0))
시간 = 폰트.render(f"초", False, (0, 0, 0))


pygame.display.set_caption("똥 피하기")
clock = pygame.time.Clock()
bg = pygame.image.load("pygame_04/img/bg.png")
bg = pygame.transform.scale(bg, (가로, 세로))

ch = pygame.image.load("pygame_04/img/ch.png")
ch_size = ch.get_rect().size
ch_가로 = ch_size[0]
ch_세로 = ch_size[1]
ch_x_pos = (가로 / 2) - (ch_가로 / 2)
ch_y_pos = 세로 - ch_세로

dd = pygame.image.load("pygame_04/img/dd.png")
dd_size = dd.get_rect().size
dd_가로 = dd_size[0]
dd_세로 = dd_size[1]
dd_x_pos = random.randint(0, 가로 - dd_가로)

ht = pygame.image.load("pygame_04/img/ht.png")
ht_size = ht.get_rect().size
ht_가로 = ht_size[0]
ht_세로 = ht_size[1]
ht_x_pos = 480 - ht_가로
ht_y_pos = 0

ht2 = pygame.image.load("pygame_04/img/ht2.png")
ht2_size = ht2.get_rect().size
ht2_가로 = ht2_size[0]
ht2_세로 = ht2_size[1]
ht2_x_pos = 480 - ht2_가로 * 2
ht2_y_pos = 0

ht3 = pygame.image.load("pygame_04/img/ht3.png")
ht3_size = ht3.get_rect().size
ht3_가로 = ht3_size[0]
ht3_세로 = ht3_size[1]
ht3_x_pos = 480 - ht3_가로 * 3
ht3_y_pos = 0

dd_y_pos = 0
dd_speed = 20
to_x = 0
ch_speed = 1.3

game_font = pygame.font.Font(None, 40)

total_time = 30

start_ticks = pygame.time.get_ticks()

running = True

while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= ch_speed
            elif event.key == pygame.K_RIGHT:
                to_x += ch_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    ch_x_pos += to_x * dt

    if ch_x_pos < 0:
        ch_x_pos = 0
    elif ch_x_pos > 가로 - ch_가로:
        ch_x_pos = 가로 - ch_가로

    dd_y_pos += dd_speed

    if dd_y_pos > 세로:
        dd_y_pos = 0
        dd_x_pos = random.randint(0, 가로 - dd_가로)

    ch_rect = ch.get_rect()
    ch_rect.left = ch_x_pos
    ch_rect.top = ch_y_pos

    dd_rect = dd.get_rect()
    dd_rect.left = dd_x_pos
    dd_rect.top = dd_y_pos

    화면.blit(bg, (0, 0))
    화면.blit(ch, (ch_x_pos, ch_y_pos))
    화면.blit(dd, (dd_x_pos, dd_y_pos))
    화면.blit(ht, (ht_x_pos, ht_y_pos))
    화면.blit(ht2, (ht2_x_pos, ht2_y_pos))
    화면.blit(ht3, (ht3_x_pos, ht3_y_pos))

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    화면.blit(timer, (5, 5))

    화면.blit(시간, (39, 12))

    if ch_rect.colliderect(dd_rect):
        print("충돌")
        hta = hta - 1
        dd_y_pos = dd_y_pos + 1000
        if hta < 3:
            ht3_y_pos = 0 - ht3_세로
            if hta < 2:
                ht2_y_pos = 0 - ht2_세로
                if hta < 1:
                    ht_y_pos = 0 - ht_세로
                    print("실패")
                    화면.blit(실패, (100, 100))
                    bb = 1
                    pygame.display.update()
                    pygame.time.delay(3000)

    if total_time - elapsed_time <= 0:
        print("성공")
        화면.blit(성공, (100, 100))
        bb = 1
        pygame.display.update()
        pygame.time.delay(3000)

    if bb == 1:
        running = False

    pygame.display.update()

pygame.QUIT()