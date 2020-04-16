import pygame.sprite
import pygame.rect
class Block(pygame.sprite.Sprite):
    def __init__(self,pos=(0,0),width=10,color=(0,0,0)):
        pygame.sprite.Sprite.__init__(self)
        self._position=[pos[0],pos[1]]
        self._width=width
        self.rect=pygame.rect.Rect(pos[0],pos[1],width,width)
        #square bloc
        self._img=pygame.Surface((width,width))
        self._img.fill(color)
    def get_position(self):
        return self._position
    def get_width(self):
        return self._width
    def set_position(self,pos):
        self._position[0]=pos[0]
        self._position[1]=pos[1]
    def get_image(self):
        return self._img

