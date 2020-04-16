from pygame.sprite import Group,spritecollide
from block import Block
class Snake(Group):
    def __init__(self):
        Group.__init__(self)
        self._head=Block((50,50))
        self._tail_position=[50,80]
        self.add(self._head,Block((50,60)),Block((50,70)),Block((50,80)))
    def get_head_position(self):
        return self._head.get_position()
    def get_head(self):
        return self._head
    def _update_head(self,direction):
         #snake goes left
        head_position=self._head.get_position()
        if(direction=='left'):
            head_position[0]-=10
            if(head_position[0]==-10):
                self._head.set_position((340,head_position[1]))
            else:
                self._head.set_position((head_position[0],head_position[1]))
        #snake goes right
        if(direction=='right'):
            head_position[0]+=10
            if(head_position[0]==350):
                self._head.set_position((0,head_position[1]))
            else:
                self._head.set_position((head_position[0],head_position[1]))
        #snake goes up
        if(direction=='up'):
            head_position[1]-=10
            if(head_position[1]==-10):
                self._head.set_position((head_position[0],390))
            else:
                self._head.set_position((head_position[0],head_position[1]))
        #snake goes down
        if(direction=='down'):
            head_position[1]+=10
            if(head_position[1]==400):
                self._head.set_position((head_position[0],0))
            else:
                self._head.set_position((head_position[0],head_position[1]))
    def eat(self,position):
            self._tail_position[0]+=10
            self.add(Block(self._tail_position))
    def collision(self,direction):
        snake_blocks_position=[block.get_position() for block in iter(self)]
        head_position=self._head.get_position()
        if(direction=='left'):
            if([head_position[0]-10,head_position[1]] in snake_blocks_position): return True
            else:return False
        elif(direction=='right'):
            if([head_position[0]+10,head_position[1]] in snake_blocks_position): return True
            else: return False
        elif(direction=='up'):
            if([head_position[0],head_position[1]-10] in snake_blocks_position): return True
            else: return False
        elif(direction=='down'):
            if([head_position[0],head_position[1]+10] in snake_blocks_position): return True
            else: return False
    def move(self,direction):
        snake_blocks=[block for block in iter(self)]
        head_position=self._head.get_position()
        #moving the body of the snake
        for i in range(1,len(snake_blocks)):
            snake_blocks[len(snake_blocks)-i].set_position(snake_blocks[len(snake_blocks)-i-1].get_position())
        #moving the head of the snake following the direction
        self._update_head(direction)
g=Snake()
