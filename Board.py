from Block import *

class Board:

    _width = 0
    _height = 0
    
    
    def __init__(self, rows, cols ):

        self.BlockList = []
        matrix = []
        
     
        for i in xrange(int(rows)):
            other = [0] * cols
            matrix.append(other)
    
        self.tray = matrix
        self._width=cols
        self._height=rows

    def __str__(self):
        s='\n' + '\n'.join([str(item) for item in self.tray])
        return s+ '\n'

    def __repr__(self):
        return self.__str__()
    
    def AddBlock(self,block):
        width=int(block.getWidth())
        height=int(block.getHeight())
        ID=block.getID()
        row_pos=int(block.getPos()[0])
        col_pos=int(block.getPos()[1])
     
        #checks to see if block can be added. account for borders or rely on IndexOutofRange?
        for i in xrange(width):
            for j in xrange(height):
                if (j+row_pos <= self._height - 1) and (i+col_pos <= self._width -1):
                    if int (self.tray[j+row_pos][i+col_pos]) ==0:
                        self.tray[j+row_pos][i+col_pos] = ID
                    else:
                        raise Exception('Block ' +str(ID) +' cannot be added at: ', i+row_pos,j+col_pos)
 
        #adds the block to the BlockList
        self.BlockList.append(block)
    
    def RemoveBlock(self, block):
        #this doesn't really 'delete' the Block object, it just removes it from the tray
 
        ID=block.getID()

        for i in xrange(width):
            for j in xrange(height):
                if int(self.tray[j+row_pos][i+col_pos]==ID):
                    self.tray[j+row_pos][i+col_pos]= 0

        #removes the block from the BlockList
        self.BlockList.remove(block)
    
    def getBlockList(self):
        return self.BlockList
         
    def PossibleMoves(self):
        '''every block may have possible moves
        so in order to make this list, go through each block
        on the board and find possible moves for it


        sum of moves for each block
        '''
        blocklist = self.getBlockList()
        allmoves={}
        for i in xrange(len(blocklist)):
            allmoves[blocklist[i]] = self.PossibleBlockMoves(blocklist[i])
        return allmoves
         
         
    def PossibleBlockMoves(self,block):
        '''is there space above it, right, left, below? '''

        pos = block.getPos()
        i = int(pos[0])
        j = int(pos[1])
        h= int(block.getHeight())
        w = int(block.getWidth())
        
        moves=[]
        
        if self.canMoveLeft(block, pos, i, j, h, w):
            moves.append("Left")
        if self.canMoveUp(block, pos, i, j, h, w):
            moves.append("Up")
        if self.canMoveDown(block, pos, i, j, h, w):
            moves.append("Down")
        if self.canMoveRight(block, pos, i, j, h, w):
            moves.append("Right")
                
        return moves      


    def canMoveLeft(self,block, pos, i, j, h, w):
        count = 0
        for  a in xrange(h):
            if j-1>=0: 
                if int(self.tray[i+a][j-1]) == 0:
                    count +=1
        if count == h:
            return True
        return False
        
    def canMoveRight(self,block, pos, i, j, h, w):
        count = 0
        for a in xrange(h):
            if j+1 <=self._width-1:
                if int(self.tray[i+a][j+1]) == 0:
                    count +=1
        if count == h:
            return True
        return False
    def canMoveUp(self,block, pos, i, j, h, w):
        count = 0
        for a in xrange(w):
            #if i+1>=self._height:
            if i-1 >=0:
                if int(self.tray[i-1][a+j]) == 0:
                    count +=1
        if count == w:
            return True
        return False


    def canMoveDown(self,block, pos, i, j, h, w):
        count = 0
        for a in xrange(w):
            if i+1 <= self._height-1:
                if int(self.tray[i+1][a+j]) == 0:
                    count +=1
        if count == w:
            return True
        return False 

     
