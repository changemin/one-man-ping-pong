import pygame as pygame
import sys, random
from pygame.locals import *


pygame.init()

#게임 플레이에 주축이 되는 변수들 정의
WINDOW_WIDTH = 300
WINDWO_HEIGHT = 600
ballX = random.randrange(0, WINDOW_WIDTH)
ballY = random.randrange(0, WINDWO_HEIGHT)
ballXSpd = 5
ballYSpd = 5
radius = 10
windowSize = [WINDOW_WIDTH,WINDWO_HEIGHT] #창 크기 설정
screen = pygame.display.set_mode(windowSize) #screen 생성
FPS = 30
clock = pygame.time.Clock()
Running = True
pygame.display.set_caption("One Man Ping Pong")

while True:
    
    pygame.draw.circle(screen, (255,0,0), (0, 0), radius) # (100, 100)을 중심으로 하는 반지름 10인 원을 그린다
    pygame.draw.circle(screen, (0,255,0), (WINDOW_WIDTH, WINDWO_HEIGHT), radius)
    
    pygame.draw.circle(screen, (0,0,255), (ballX, ballY), radius)
    pygame.draw.circle(screen, (0,0,0), (ballX, ballY), radius)
    ballX += ballXSpd
    ballY += ballYSpd
    if(ballX + radius >= WINDOW_WIDTH or ballX - radius <= 0): #벽 충돌 이벤트 검사
        ballXSpd *= -1
    if(ballY + radius >= WINDWO_HEIGHT or ballY - radius <= 0): #벽 충돌 이벤트 검사
        ballYSpd *= -1
    pygame.draw.circle(screen, (0,0,255), (ballX, ballY), radius)
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
    