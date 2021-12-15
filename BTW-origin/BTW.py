import sys
import pygame
import random
import time
from pygame.event import Event
"""-*- coding:uft-8 -*-"""
"""
Supported By AkiyamaAya
Start date:2021/11/28
End date:Unknown
"""
#Present From AkiyamaAya
from pygame.locals import *
def Hajimeru():
    pygame.init()
    screen = pygame.display.set_mode((1080,1080))
    icor=pygame.image.load("./gfx/BTW.png")
    backg=pygame.image.load("./gfx/background.png").convert_alpha()
    screen.blit(backg,(-750,0))
    pygame.display.set_icon(icor)
    you=pygame.image.load("./gfx/you2.png").convert_alpha()
    screen.blit(you,(540,800))
    pygame.display.set_caption('Battle With Witch ver.4.0')
    position = you.get_rect()
    pygame.display.update()
    v=4
    site=[540,800]
    while 1:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.flip()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    iif=False
            if keys[K_LSHIFT]:
                v=2
            if not keys[K_LSHIFT]:
                v=4
            if event.type==pygame.KEYDOWN:
                iif=True
                if keys[K_RIGHT]:
                    site[0]+=v
                    pygame.key.set_repeat(10)
                if keys[K_LEFT]:
                    site[0]-=v
                    pygame.key.set_repeat(10)
                if keys[K_UP]:
                    site[1]-=v
                    pygame.key.set_repeat(10)
                if keys[K_DOWN]:
                    site[1]+=v
                    pygame.key.set_repeat(10)
                screen.blit(backg,(-750,0))
            if site[0]<20:
                site[0]=20
            if site[0]>1040:
                site[0]=1040
            if site[1]<20:
                site[1]=20 
            if site[1]>1040:
                site[1]=1040
        screen.blit(you,(site[0],site[1]))
        position = position.move(site)
        
        screen.blit(you,position)
        pygame.display.flip()
Hajimeru()
class player:
    health=3
    p_y=0
    p_x=0
