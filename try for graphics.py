import pygame, sys, random
from time import*
pygame.init()
windowSurface=pygame.display.set_mode(((600, 600)), 5, 6)
pygame.display.set_caption("BOUNCING Ball")
BLACK=(0,0,0)
W=(255,255,255)
R=(255,0,0)
G=(0,255,0)
B=(0,0,255)
info=pygame.display.Info()
sw=info.current_w
sh=info.current_h
y=10
x=20
s1=s2=20
direction=1
pygame.draw.circle(windowSurface, W, (x, y), s1, s2)
pygame.display.update()