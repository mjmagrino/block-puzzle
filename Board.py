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
        width=int(block.getWidth())
        height=int(stryblock.getHeight())
        #ID=block.getID
        row_pos=int(block.getPos()[0])
        col_pos=int(block.getPos()[1])
     
        #checks to see if block can be added. borders accounted for?
        for i in range(width):
            for j in range(height):
                if int (self.tray[i+row_pos][j+col_pos]) !=0:
                    raise Exception('Block cannot be added at: ', i+row_pos,j+col_pos)

        #adds the block
        for i in range(width):
            for j in range(height):
                self.tray[i+row_pos][j+col_pos] = ID
    
    
    #RemoveBlock and MoveBlock are depreciated. Each new config will result in a new Board.
    #This will be handled in Puzzle.py
'''    def RemoveBlock(self, block, ID):
        #this doesn't really 'delete' the Block object, it just removes it from the tray
        #should be renamed to 'RemoveBlock()'...
        width=int(block.getWidth())
        height=int(block.getHeight())
        #ID=block.getID
        row_pos=int(block.getPos()[0])
        col_pos=int(block.getPos()[1])
          
        for i in range(width):
            for j in range(height):
                if int(self.tray[i+row_pos][j+col_pos]==ID):
                    self.tray[i+row_pos][j+col_pos]= 0
    
  
    def MoveBlock(self,block,ID,direction):
         #intial thought: create temp block, delete old block, add temp block...
         #this is really stupid and will wind up with a ton of extraneous memory usage
         #it would be better to change the position information in the block rather than create
         #a ton of new Block objects.
       
         # alternate way: take direction as arg...must handle 4 cases
       	if direction == 'right':
        	block.setPos(block.getPos()[0],block.getPos()[1]+1)
       	elif direction == 'left':
       		block.setPos(block.getPos()[0],block.getPos()[1]-1)
       	elif direction == 'up':
        	block.setPos(block.getPos()[0]-1,block.getPos()[1])
        elif direction == 'down':
        	block.setPos(block.getPos()[0]+1,block.getPos()[1])
        else:
        	raise Exception("MoveBlock failed!")
 '''
       
    
     
         
    
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


def test():
    b = Board(3,5)
    print("This is a test 3x5 Board called 'b'\n")
    print(b)

    b1= Block(2,2,0,0)
    b.AddBlock(b1,1)
    print("Add a 2x2 test block called 1 to the top left corner of 'b'\n")
    print(b)

    b2 = Block(1,2,0,3)
    b.AddBlock(b2,3)
    print("Add a 1x2 test block called 2 to the top right corner of 'b'\n")
    print(b)

    #print("Attempt to add a 1x1 test block called 3 to an already occupied spot\n")
    #b3= Block(1,1,0,0)
    #b.AddBlock(b3,3)
    #print(b)

    #print("Attempt to add a 1x1 test block called 4 to an out of bound spot\n")
    #b4= Block(1,1,5,5)
    #b.AddBlock(b4,4)
    #print(b)

    
    #b.MoveBlock(b2,3,'down')
    #print(b)

    #b.MoveBlock(b2,3,'left')
    #print(b)



b= test()

