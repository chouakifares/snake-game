import pygame.surface,pygame.display,pygame.key,pygame.event
from pygame import Color
from snake import Snake
from time import sleep
from random import randint
class Grid(pygame.surface.Surface):
    def __init__(self,dimesion,snake):
        pygame.surface.Surface.__init__(self,dimesion)
        self._snake=snake
        self._dimension=dimesion
        self.current_food=[0,0]
    def draw_grid(self):
        #painting the background in white
        self.fill((255,255,255))
        #drawing the borders
        pygame.draw.lines(self,(0,0,0),True,[(0,0),(self.get_width()-1,0),(self.get_width()-1,self.get_height()-1),(0,self.get_height()-1)])
        path=[0,10]
        #seperationg and drawing the grid
        for i in range(0,self.get_height(),10):
            pygame.draw.line(self,(0,0,0),(i,0),(i,self.get_height()-1))
            pygame.draw.line(self,(0,0,0),(0,i),(self.get_width(),i))
        for i in self._snake:
            self.blit(i.get_image(),i.get_position())
        #drawing the food
        self.fill((255,0,0),(self.current_food[0],self.current_food[1],10,10))
    def generate_food(self):
        snake_blocks_position=[block.get_position() for block in iter(self._snake)]
        i=randint(0,(self._dimension[0]-10)/10)*10
        j=randint(0,(self._dimension[1]-10)/10)*10
        while([i,j]==self.current_food or [i,j] in snake_blocks_position):
            i=randint(0,(self._dimension[0]-10)/10)*10
            j=randint(0,(self._dimension[1]-10)/10)*10
        self.current_food=[i,j] 
def init():
    pygame.display.init()
    s=Snake()
    grid=Grid((350,400),s)
    grid.draw_grid()
    screen=pygame.display.set_mode((400,450))
    screen.blit(grid,(25,25))
    pygame.event.set_blocked([pygame.MOUSEMOTION,pygame.KEYUP,pygame.MOUSEBUTTONUP,pygame.MOUSEBUTTONDOWN,pygame.ACTIVEEVENT])
    return (screen,grid,s)
(screen,grid,s)=init()
d='up'
while not s.collision(d):
    e=pygame.event.get()
    if(len(e)>0 and e[0].type==pygame.KEYDOWN):
        if(d!="right" and e[0].key==pygame.K_LEFT):
            d="left"
        elif(d!="up" and  e[0].key==pygame.K_DOWN):
            d="down"
        elif(d!="left" and  e[0].key==pygame.K_RIGHT):
            d="right"
        elif(d!="down" and e[0].key==pygame.K_UP):
            d="up"
    s.move(d)
    grid.draw_grid()
    screen.blit(grid,(25,25))
    if(s.get_head_position()==grid.current_food):
        s.eat(grid.current_food)
        grid.generate_food()
    pygame.display.flip()
    sleep(0.05)
EndScreen=pygame.surface.Surface((400,450))
c=pygame.Color(40,40,40)
EndScreen.fill(c)
EndScreen.set_alpha(125)
print(c.a)
screen.blit(EndScreen,(0,0))
pygame.display.flip()
