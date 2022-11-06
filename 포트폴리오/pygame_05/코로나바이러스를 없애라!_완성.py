import pygame as pg
import random


def 볼초기화():
    global 랜덤볼, 랜덤볼좌표
    랜덤볼 = [볼] * 4 + [코로나볼] * 5
    랜덤볼좌표 = [(120 + x * 220, 185 + y * 170)
             for x in range(3) for y in range(3)]
    random.shuffle(랜덤볼)


pg.init()


화면가로길이, 화면세로길이 = (780, 740)
화면 = pg.display.set_mode([화면가로길이, 화면세로길이])
pg.display.set_caption('코로나 바이러스를 없애라!')

글꼴 = pg.font.SysFont('malgungothic', 30)
배경이미지 = pg.image.load('pygame_05/img/백신_배경.jpg')
배경이미지 = pg.transform.scale(배경이미지, (화면가로길이, 화면세로길이))
화면.blit(배경이미지, (0, 0))

시간바 = pg.image.load('pygame_05/img/시간바.png')
시간바 = pg.transform.scale(시간바, (250, 65))
화면.blit(시간바, (520, 20))

볼 = pg.image.load('pygame_05/img/볼.png')
볼 = pg.transform.scale(볼, (100, 100))

코로나볼 = pg.image.load('pygame_05/img/코로나볼.png')
코로나볼 = pg.transform.scale(코로나볼, (100, 100))

pg.display.update()

볼초기화()

경과시간 = 0
볼생성시간 = 0
볼인덱스 = 0

시계 = pg.time.Clock()
현재챕터 = 1
최종챕터 = 3

while True:
    if 현재챕터 <= 최종챕터:
        화면.blit(배경이미지, (0, 0))
        화면.blit(시간바, (520, 20))

        흐른시간 = 시계.tick(60) / 1000
        경과시간 += 흐른시간

        if 경과시간 <= 60:
            시간문자열 = f'{round(경과시간, 1)} 초'
        else:
            시간문자열 = f'{int(경과시간 // 60)}분 {int(경과시간 % 60)}초'

        시간 = 글꼴.render(시간문자열, True, (0, 0, 0))
        화면.blit(시간, (620, 32))

        챕터글자 = 글꼴.render(f'챕터 : {현재챕터} / {최종챕터}', True, (255, 255, 255))
        화면.blit(챕터글자, (80, 20))

        볼글자 = 글꼴.render(
            f'남은 코로나볼 갯수 : {len(랜덤볼) - 랜덤볼.count(볼)}개', True, (255, 255, 255))
        화면.blit(볼글자, (80, 90))

        볼생성시간 += 흐른시간
        if 볼생성시간 >= 1:
            볼생성시간 = 0
            볼인덱스 = random.randrange(len(랜덤볼))

        현재볼 = 화면.blit(랜덤볼[볼인덱스], 랜덤볼좌표[볼인덱스])
    else:
        화면.fill((255, 255, 255))
        종료멘트 = 글꼴.render(
            f'경과시간은 {경과시간//60}분 {round(경과시간%60, 2)}초 입니다.', True, (0, 0, 0))
        화면.blit(종료멘트, (화면가로길이 / 2 - 230, 화면세로길이 / 2 - 80))

    pg.display.update()

    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            pg.display.quit()
        elif 이벤트.type == pg.MOUSEBUTTONDOWN:
            클릭_위치 = pg.mouse.get_pos()
            if 볼인덱스 != -1 and 현재볼.collidepoint(클릭_위치):
                if 랜덤볼[볼인덱스] == 코로나볼:
                    랜덤볼[볼인덱스] = 볼

                    if len(랜덤볼) - 랜덤볼.count(볼) == 0:
                        현재챕터 += 1
                        볼초기화()
