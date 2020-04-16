import pygame
from time import sleep
import os
def draw_grid(surface,snake=[]):
    surface.fill((255,255,255))
    pygame.draw.lines(surface,(0,0,0),True,[(0,0),(surface.get_width()-1,0),(surface.get_width()-1,surface.get_height()-1),(0,surface.get_height()-1)])
    path=[0,10]
    for i in range(0,surface.get_height(),10):
        pygame.draw.line(surface,(0,0,0),(i,0),(i,surface.get_height()-1))
        pygame.draw.line(surface,(0,0,0),(0,i),(surface.get_width(),i))
    for cordo in snake:
        surface.fill((0,0,0),(cordo[0],cordo[1],10,10))
def direction(i,snake):
    #snake goes left
    if(i=='left'):
        snake[0][0]-=10
    #snake goes right
    if(i=='right'):
        snake[0][0]+=10
    #snake goes up
    if(i=='up'):
        snake[0][1]-=10
    #snake goes down
    if(i=='down'):
        snake[0][1]+=10
pygame.display.init()
grid=pygame.Surface((350,400))
screen=pygame.display.set_mode((400,450))
screen.fill((205,205,205))
screen.blit(grid,(25,25))
snake=[[230,50],[240,50],[250,50],[260,50],[260,50],[260,60],[260,70],[260,80],[260,90],[260,100],[260,110],[250,110],[240,110],[230,110],[220,110],[210,110]]
draw_grid(grid)
screen.blit(grid,(25,25))
pygame.display.flip()
d='left'
a=0.1
while True:
    draw_grid(grid,snake)
    for i in range(1,len(snake)):
            snake[len(snake)-i][0]=snake[len(snake)-i-1][0]
            snake[len(snake)-i][1]=snake[len(snake)-i-1][1]
    direction(d,snake)
    screen.blit(grid,(25,25))
    pygame.display.flip()
    sleep(a)
    a-=0.0001
    if(snake[0][0]==0 and snake[0][1]==0):
        if(d=='left'):
            d='down'
        else:
            d='right'
    elif(snake[0][0]==0 and snake[0][1]==390):
        if(d=='down'):
            d='right'
        else:
            d='up'
    elif(snake[0][0]==340 and snake[0][1]==0):
        if(d=='right'):
            d='down'
        else:
            d='left'            
    elif(snake[0][0]==340 and snake[0][1]==390):
        if(d=='right'):
            d='up'
        else:
            d='left'
    elif(snake[0][0]==340):
        d='up'
    elif(snake[0][0]==0):
        d='down'
    elif(snake[0][1]==0):
        d='left'
    elif(snake[0][1]==390):
        d='right'
     
