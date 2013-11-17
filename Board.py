from Block import *

class Board:

    _width = 0
    _height = 0
    
    
    def __init__(self, rows, cols ):

        self.BlockList = []
        matrix = []
        
     
        for i in range(int(rows)):
            other = [0] * cols
            matrix.append(other)
    
        self.tray = matrix
        self._width=cols
        self._height=rows

    def __str__(self):
        #old code
        '''
        tmp1= self.tray
        
        for row in tmp1:
            print(row)
        return ''
        '''
        #I think that this is cleaner:
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
        for i in range(width):
            for j in range(height):
                if int (self.tray[j+row_pos][i+col_pos]) !=0:
                    raise Exception('Block ' +str(ID) +' cannot be added at: ', i+row_pos,j+col_pos)

        #sets the block ID to appear in the proper location in the tray
        for i in range(width):
            for j in range(height):
                self.tray[j+row_pos][i+col_pos] = ID
    
        #adds the block to the BlockList
        self.BlockList.append(block)
    
    def RemoveBlock(self, block):
        #this doesn't really 'delete' the Block object, it just removes it from the tray
             #most specific info about the block not currently needed
        
        #width=int(block.getWidth())
        #height=int(block.getHeight())
        ID=block.getID()
        #row_pos=int(block.getPos()[0])
        #col_pos=int(block.getPos()[1])
          
        for i in range(width):
            for j in range(height):
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
        for i in range(len(blocklist)):
            allmoves[blocklist[i]] = self.PossibleBlockMoves(blocklist[i])
        return allmoves
         
         
    def PossibleBlockMoves(self,block):
        '''is there space above it, right, left, below? '''

        moves=[]
        if self.canMoveLeft(block):
            moves.append("Left")
        if self.canMoveUp(block):
            moves.append("Up")
        if self.canMoveDown(block):
            moves.append("Down")
        if self.canMoveRight(block):
            moves.append("Right")
                
        return moves      


    def canMoveLeft(self,block):

        pos = block.getPos()
        i = int(pos[0])
        j = int(pos[1])
        h= int(block.getHeight())
        w = int(block.getWidth())
        #print("height of block " + str(block.getID()) + " is: " + str(h))
        #print("width of block " + str(block.getID()) + " is: " + str(w))
        count = 0
        for  a in range(h):
            if j-1>=0:
                #print("spot to the left of " +str(block.getID()) +": "+ str(self.tray[i+a][j-1]))  
                if int(self.tray[i+a][j-1]) == 0:
                    count +=1
        if count == h:
            return True
        return False
        
    def canMoveRight(self,block):

        pos = block.getPos()
        i = int(pos[0])
        j = int(pos[1])
        h= int(block.getHeight())
        w = int(block.getWidth())
        count = 0
        for a in range(h):
            if j+1 <=self._width:
                if int(self.tray[i+a][j+1]) == 0:
                    count +=1
        if count == h:
            return True
        return False
    def canMoveUp(self,block):

        pos = block.getPos()
        i = int(pos[0])
        j = int(pos[1])
        h= int(block.getHeight())
        w = int(block.getWidth())
        
        count = 0
        for a in range(w):
            if i+1>=self._height:
                #print("spot above " +str(block.getID()) +": "+ str((self.tray[i-1][a+j])))
                if int(self.tray[i-1][a+j]) == 0:
                    count +=1
        if count == w:
            return True
        return False


    def canMoveDown(self,block):
        pos = block.getPos()
        i = int(pos[0])
        j = int(pos[1])
        h= int(block.getHeight())
        w = int(block.getWidth())
        count = 0
        for a in range(w):
            if i+1 <= self._height-1:
                #print("spot below " +str(block.getID()) +": "+ str((self.tray[i+1][a+j])))
                if int(self.tray[i+1][a+j]) == 0:
                    count +=1
        if count == w:
            return True
        return False 

     
