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
FPS = 10

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
        self.WallColli = 0
    def draw(self):
        pygame.draw.circle(screen, colors["ball"], (self.x, self.y), self.radius)
        self.x += self.XSpd
        self.y += self.YSpd
    def collisionCheck(self):
        pygame.draw.circle(screen, (255,255,255), (75,75), self.radius)
        pygame.draw.circle(screen, (255,255,255), (75,125), self.radius)
        pygame.draw.circle(screen, (255,255,255), (50,100), self.radius)
        pygame.draw.circle(screen, (255,255,255), (100,100), self.radius)
        if(self.x + self.radius >= WINDOW_WIDTH or self.x - self.radius <= 0): #벽 충돌 이벤트
            self.XSpd *= -1
            self.WallColli += 1
        elif(self.y + self.radius >= WINDOW_HEIGHT or self.y - self.radius <= 0): #벽 충돌 이벤트
            self.YSpd *= -1
            self.WallColli += 1
        elif(self.x >= PaddleTOP.x - PaddleTOP.length/2 and self.x <= PaddleTOP.x + PaddleTOP.length/2): #상단 패들과 충돌 검사
            pygame.draw.circle(screen, (255,0,0), (75,75), self.radius)
            if(self.y - self.radius <= PaddleTOP.y + PaddleTOP.thickness/2):
                pygame.draw.circle(screen, (0,0,255), (75,75), self.radius)
                self.YSpd *= -1
                self.WallColli += 1
        elif(self.x >= PaddleBOTTOM.x - PaddleBOTTOM.length/2 and self.x <= PaddleBOTTOM.x + PaddleBOTTOM.length/2): #하단 패들과 충돌 검사
            pygame.draw.circle(screen, (255,0,0), (75,125), self.radius)
            if(self.y + self.radius >= PaddleBOTTOM.y - PaddleBOTTOM.thickness/2):
                pygame.draw.circle(screen, (0,0,255), (75,125), self.radius)
                self.YSpd *= -1
                self.WallColli += 1
        elif(self.y >= PaddleLEFT.y - PaddleLEFT.length/2 and self.y <= PaddleLEFT.y + PaddleLEFT.length/2): #왼쪽 패들과 충돌 검사
            pygame.draw.circle(screen, (255,0,0), (50,100), self.radius)
            if(self.x - self.radius <= PaddleLEFT.x + PaddleLEFT.thickness/2):
                pygame.draw.circle(screen, (0,0,255), (50,100), self.radius)
                self.XSpd *= -1
                self.WallColli += 1
        elif(self.y >= PaddleRIGHT.y - PaddleRIGHT.length/2 and self.y <= PaddleRIGHT.y + PaddleRIGHT.length/2): #오른쪽 패들과 충돌 검사
            pygame.draw.circle(screen, (255,0,0), (50,100), self.radius)
            if(self.x + self.radius >= PaddleRIGHT.x - PaddleRIGHT.thickness/2):
                pygame.draw.circle(screen, (0,0,255), (50,100), self.radius)
                self.XSpd *= -1
                self.WallColli += 1

class Paddle:
    def __init__(self, x, y, length, thickness):
        self.x = x
        self.y = y
        self.length = length
        self.thickness = thickness
    def drawTOP(self):
        self.x = mousex
        pygame.draw.line(screen, colors["paddle"],[self.x-(self.length/2),self.y],[self.x+(self.length/2),self.y],self.thickness)
    def drawBOTTOM(self):
        self.x = WINDOW_WIDTH-mousex
        pygame.draw.line(screen, colors["paddle"],[self.x-(self.length/2),self.y],[self.x+(self.length/2),self.y],self.thickness)
    def drawLEFT(self):
        self.y = mousey
        pygame.draw.line(screen, colors["paddle"],[self.x,self.y-(self.length/2)],[self.x,self.y+(self.length/2)],self.thickness)
    def drawRIGHT(self):
        self.y = WINDOW_HEIGHT-mousey
        pygame.draw.line(screen, colors["paddle"],[self.x,self.y-(self.length/2)],[self.x,self.y+(self.length/2)],self.thickness)

Ball = Ball(random.randrange(10,WINDOW_WIDTH-10),random.randrange(10,WINDOW_HEIGHT-10),10,4) #게임공
PaddleTOP = Paddle(random.randrange(0,WINDOW_WIDTH),30,100,14) #위쪽 패들
PaddleBOTTOM = Paddle(random.randrange(0,WINDOW_WIDTH),WINDOW_HEIGHT-30,100,14) #아랫쪽 패들
PaddleLEFT = Paddle(30,random.randrange(0,WINDOW_HEIGHT),100,14) #왼쪽 패들
PaddleRIGHT = Paddle(WINDOW_WIDTH-30,random.randrange(0,WINDOW_HEIGHT),100,14) #오른쪽 패들
mousex = 0
mousey = 0

while True:
    screen.fill(colors["background"])
    PaddleTOP.drawTOP()
    PaddleBOTTOM.drawBOTTOM()
    PaddleLEFT.drawLEFT()
    PaddleRIGHT.drawRIGHT()
    Ball.draw()
    Ball.collisionCheck()

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE): #esc또는 X를 눌렀을 때 게임 종료
            pygame.quit()
            sys.exit()

    mousex,mousey = pygame.mouse.get_pos()
    print("("+str(mousex)+","+str(mousey)+") Wall Collision : "+str(Ball.WallColli)) # 마우스 위치 Logging
    pygame.draw.circle(screen, (255,0,0), (mousex, mousey), 5) #마우스 위치 표시
    pygame.display.flip()
    FPSclock.tick(FPS)
    