import pygame as pygame
import sys
from pygame.locals import *


pygame.init()

windowSize = [400,300] #창 크기 설정
screen = pygame.display.set_mode(windowSize) #screen 생성
FPS = 30
clock = pygame.time.Clock()
pygame.display.set_caption("One Man Ping Pong")

while True:
    
    pygame.draw.circle(screen, (255,0,0), (0, 0), 10) # (100, 100)을 중심으로 하는 반지름 10인 원을 그린다
    pygame.draw.circle(screen, (0,255,0), (400, 300), 10)
    for event in pygame.event.get(): #event get
        if not hasattr(event, 'key'):
            continue
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                print("KEY RIGHT")
            if event.key == K_LEFT:
                print("KEY LEFT")
        '''if event.type == pygame.MOUSEMOTION:
            print("mouse move "+event.pos)'''

    for event in pygame.event.get(): # 종료 이벤트
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    clock.tick(FPS)
    