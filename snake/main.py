import classes.grid 
import pygame.display
pygame.display.init()
s=Snake()
grid=Grid((350,400),s)
grid.draw_grid()
screen=pygame.display.set_mode((400,450))
screen.blit(grid,(25,25))
while True:
    pygame.display.flip()
    s.move("right")
    grid.draw_grid()
    screen.blit(grid,(25,25))
    sleep(0.1)
