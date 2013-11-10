class Board:

    def __init__(self, rows, cols ):

        matrix = []
        
     
        for i in range(int(rows)):
            other = [0] * cols
            matrix.append(other)

        self.tray = matrix

    def __str__(self):

        tmp1= self.tray
        
        for row in tmp1:
            print(row)
        return ''

           
    def AddBlock(self,block,ID):
        width=block.getWidth
        height=block.getHeight
        #ID=block.getID
        row_pos=block.getPos[0]
        col_pos=block.getPos[1]
     
        #checks to see if block can be added. borders accounted for?
        for i in range(width):
	    for j in range(height):
		if int (self.tray[i+row_pos][j+col_pos]) !=0:
		    raise Exception('Block cannot be added at: ', i+row_pos,j+col_pos)

        #adds the block
        for i in range(width):
            for j in range(height):
                self.tray[i+row_pos][j+col_pos] = ID
    
    def DeleteBlock(self, block, ID):
          for i in range(width):
              for j in range(height):
                  if int(self.tray[i+row_pos][j+col_pos]==ID
                       self.tray[i+row_pos][j+col_pos]= 0
    def MoveBlock(self,block,ID):
          DeleteBlock(block, ID)
          
    def PossibleMoves(self,blocklist):
        '''every block may have possible moves
        so in order to make this list, go through each block
        on the board and find possible moves for it

        sum of moves for each block
        '''
        allmoves={}
        for i in range(len(blocklist)):
            allmoves[blocklist[i]] = PossibleBlockMoves(blocklist[i])
        return allmoves
         

         
    def PossibleBlockMoves(self,block):
        '''is there space above it, right, left, below? '''

        moves=[]
        if canMoveLeft(block):
            moves.append("Left")
        if canMoveUp(block):
            moves.apend("Up")
        if canMoveDown(block):
            moves.append("Down")
        if canMoveRight(block):
            moves.append("Right")
                
        return moves      

    def canMoveLeft(self,block): 

        pos = block.getPos()
        i = pos[0]
        j = pos[1]
        h= block.getHeight()
        w = block.getWidth()
        count = 0
        for  a in range(h):
            if int(matrix[i+a][j-1]) == 0:
                count +=1
        if count == h:
            return True
        return False
        
    def canMoveRight(self,block):

        pos = block.getPos()
        i = pos[0]
        j = pos[1]
        h= block.getHeight()
        w = block.getWidth()
        count = 0
        for a in range(h):
            if int(matrix[i+a][j+1]) == 0:
                count +=1
        if count == h:
            return True
        return False
    def canMoveUp(self,block):

        pos = block.getPos()
        i = pos[0]
        j = pos[1]
        h= block.getHeight()
        w = block.getWidth()
        count = 0
        for a in range(w):
            if int(matrix[i-1][a+j]) == 0:
                count +=1
        if count == h:
            return True
        return False

    def canMoveDown(self,block):
        pos = block.getPos()
        i = pos[0]
        j = pos[1]
        h= block.getHeight()
        w = block.getWidth()
        count = 0
        for a in range(w):
            if int(matrix[i+1][a+j]) == 0:
                count +=1
        if count == h:
            return True
        return False 

        
class Block:

    _width = 0
    _height = 0
    _row_pos = 0
    _col_pos = 0
    
    def __init__(self,width,height,row_pos,col_pos):

        self._width = width
        self._height = height
        self._col_pos = col_pos
        self._row_pos = row_pos

    def isequal(other):
  
        return (self._width == other._width) and (self._height == other._height)

    def getSize(self):
        return self.getHeight(),self.getWidth()

    def getPos(self):
        return self._row_pos,self._col_pos

    def getHeight(self):
        return self._height

    def getWidth(self):
        return self._width
    '''def __str__(self):
	return ' Width: '+ str(self._width ) +\
		' Height: '+str(self._height) +\
		' Row_pos: '+str(self._row_pos) +\
		' Col_pos: '+str(self._col_pos)+'\n'

    def __repr__(self):
	return self.__str__()'''
