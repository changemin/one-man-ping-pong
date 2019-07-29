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
WINDWO_HEIGHT = 600
ballX = random.randrange(0, WINDOW_WIDTH)
ballY = random.randrange(0, WINDWO_HEIGHT)
ballXSpd = 5
ballYSpd = 5
radius = 10
windowSize = [WINDOW_WIDTH,WINDWO_HEIGHT] #창 크기 설정
screen = pygame.display.set_mode(windowSize) #screen 생성
FPS = 60

clock = pygame.time.Clock()
Running = True
pygame.display.set_caption("One Man Ping Pong")

class Paddle:
    def __init__(self, location, length, thickness):
        self.location = location
        self.length = length
        self.thickness = thickness

PaddleTOP = Paddle(random.randrange(0,WINDOW_WIDTH),50,10)
while True:
    screen.fill(colors["background"])
    pygame.draw.circle(screen, colors["ball"], (ballX, ballY), radius)
    pygame.draw.circle(screen, colors["background"], (ballX, ballY), radius) #다시 지우기
    pygame.draw.line(screen, colors["paddle"],[PaddleTOP.location-(PaddleTOP.length/2),30],[PaddleTOP.location+(PaddleTOP.length/2),30],30)
    ballX += ballXSpd
    ballY += ballYSpd
    print("X:" + str(ballX) +" Y:"+str(ballY))
    if(ballX + radius >= WINDOW_WIDTH or ballX - radius <= 0): #벽 충돌 이벤트 검사
        ballXSpd *= -1
    if(ballY + radius >= WINDWO_HEIGHT or ballY - radius <= 0): #벽 충돌 이벤트 검사
        ballYSpd *= -1
    pygame.draw.circle(screen, colors["ball"], (ballX, ballY), radius)
    for event in pygame.event.get(): #event get
        if not hasattr(event, 'key'):
            continue
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                print("KEY RIGHT")
            elif event.key == K_LEFT:
                print("KEY LEFT")
            elif event.key == K_ESCAPE:
                sys.exit()
                pygame.quit()
        '''if event.type == pygame.MOUSEMOTION:
            print("mouse move "+event.pos)'''
        if event.type == QUIT:
            sys.exit()
            pygame.quit()

    pygame.display.flip()
    clock.tick(FPS)
    