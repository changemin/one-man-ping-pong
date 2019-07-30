import pygame as pygame
import sys, random
from pygame.locals import *


pygame.init()

colors = {
    "background":[250,227,217],
    "ball":[255,182,185],
    "paddle":[187,222,214]
}
#게임 플레이에 주축이 되는 변수들 정의
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
windowSize = [WINDOW_WIDTH,WINDOW_HEIGHT] #창 크기 설정
screen = pygame.display.set_mode(windowSize) #screen 생성
FPS = 60

FPSclock = pygame.time.Clock()
Running = True
pygame.display.set_caption("One Man Ping Pong")

class Ball:
    def __init__(self, x, y, radius, Spd):
        self.x = x
        self.y = y
        self.radius = radius
        self.XSpd = Spd
        self.YSpd = Spd
    def draw(self):   
        pygame.draw.circle(screen, colors["ball"], (self.x, self.x), self.radius)
        self.x += self.XSpd
        self.y += self.YSpd
    def collisionCheck(self):
        if(self.x + self.radius >= WINDOW_WIDTH or self.x - self.radius <= 0): #벽 충돌 이벤트 검사
            self.XSpd *= -1
        if(self.y + self.radius >= WINDOW_HEIGHT or self.y - self.radius <= 0): #벽 충돌 이벤트 검사
            self.YSpd *= -1

class Paddle:
    def __init__(self, locationX, locationY, length, thickness):
        self.locationX = locationX
        self.locationY = locationY
        self.length = length
        self.thickness = thickness
    def draw(self):
        self.locationX = mousex
        pygame.draw.line(screen, colors["paddle"],[self.locationX-(self.length/2),self.locationY],[self.locationX+(self.length/2),self.locationY],self.thickness)

Ball = Ball(random.randrange(10,WINDOW_WIDTH-10),random.randrange(10,WINDOW_HEIGHT-10),10,5) #게임공
PaddleTOP = Paddle(random.randrange(0,WINDOW_WIDTH),30,100,14) #스크린 위쪽 패들
PaddleBOTTOM = Paddle(random.randrange(0,WINDOW_WIDTH),WINDOW_HEIGHT-30,100,14)
mousex = 0
mousey = 0
while True:

    screen.fill(colors["background"])
    PaddleTOP.draw()
    PaddleBOTTOM.draw()
    Ball.draw()
    Ball.collisionCheck()

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE): #esc또는 X를 눌렀을 때 게임 종료
            pygame.quit()
            sys.exit()

    mousex,mousey = pygame.mouse.get_pos()
    print("("+str(mousex)+ ","+str(mousey)+")") # 마우스 위치 Logging
    pygame.draw.circle(screen, (255,0,0), (mousex, mousey), 5) #마우스 위치 표시
    pygame.display.flip()
    FPSclock.tick(FPS)
    