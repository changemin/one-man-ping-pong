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
ballX = random.randrange(0, WINDOW_WIDTH)
ballY = random.randrange(0, WINDOW_HEIGHT)
ballXSpd = 5
ballYSpd = 5
radius = 10
windowSize = [WINDOW_WIDTH,WINDOW_HEIGHT] #창 크기 설정
screen = pygame.display.set_mode(windowSize) #screen 생성
FPS = 60

FPSclock = pygame.time.Clock()
Running = True
pygame.display.set_caption("One Man Ping Pong")

class Paddle:
    def __init__(self, locationX, locationY, length, thickness):
        self.locationX = locationX
        self.locationY = locationY
        self.length = length
        self.thickness = thickness
    def draw(self):
        self.locationX = mousex
        pygame.draw.line(screen, colors["paddle"],[self.locationX-(self.length/2),self.locationY],[self.locationX+(self.length/2),self.locationY],self.thickness)

PaddleTOP = Paddle(random.randrange(0,WINDOW_WIDTH),30,100,14) #스크린 위쪽 패들
PaddleBOTTOM = Paddle(random.randrange(0,WINDOW_WIDTH),WINDOW_HEIGHT-30,100,14)
mousex = 0
mousey = 0
while True:

    screen.fill(colors["background"])
    pygame.draw.circle(screen, colors["ball"], (ballX, ballY), radius)
    PaddleTOP.draw()
    PaddleBOTTOM.draw()
    ballX += ballXSpd
    ballY += ballYSpd
    
    if(ballX + radius >= WINDOW_WIDTH or ballX - radius <= 0): #벽 충돌 이벤트 검사
        ballXSpd *= -1
    if(ballY + radius >= WINDOW_HEIGHT or ballY - radius <= 0): #벽 충돌 이벤트 검사
        ballYSpd *= -1
    pygame.draw.circle(screen, colors["ball"], (ballX, ballY), radius)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        '''elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                print("right")
            elif event.key == K_LEFT:
                print("left")'''
    mousex,mousey = pygame.mouse.get_pos()
    print("("+str(mousex)+ ","+str(mousey)+")") # 마우스 위치 Logging
    pygame.draw.circle(screen, (255,0,0), (mousex, mousey), 5) #마우스 위치 표시
    pygame.display.flip()
    FPSclock.tick(FPS)
    