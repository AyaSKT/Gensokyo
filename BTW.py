import sys
import pygame
import random
import time
from pygame.event import Event
from pygame.locals import *
def Hajimari():
    pygame.init()
    witch=pygame.image.load("./gfx/abc.png")
    screen = pygame.display.set_mode((1080,900))
    ico=pygame.image.load("./gfx/BTW.png")
    backg=pygame.image.load("./gfx/background.png").convert_alpha()
#    health_blank = pygame.image.load("./gfx/Health_Blank")
    screen.blit(backg,(-1450,0))
    pygame.display.set_icon(ico)
    you=pygame.image.load("./gfx/you2.png").convert_alpha()
    screen.blit(you,(540,800))
    pygame.display.set_caption('Battle With Witch 4.0')
    position = you.get_rect()
    wposition=witch.get_rect()
    screen.blit(witch,(500,100))
    pygame.display.update()
    v=4
    site=[540,800]
    wsite=[500,100]
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
            if site[0]<20:
                site[0]=20
            if site[0]>1040:
                site[0]=1040
            if site[1]<20:
                site[1]=20 
            if site[1]>860:
                site[1]=860
            screen.blit(backg,(-1450,0))
            screen.blit(you,(site[0],site[1]))
            screen.blit(witch,(wsite[0],wsite[1]))
            position = position.move(site);wposition=wposition.move(wsite)
            
            screen.blit(witch,wposition);screen.blit(you,position)
            
            pygame.display.flip()
Hajimari()
