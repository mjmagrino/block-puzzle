class Board:

    _width = 0
    _height = 0
    def __init__(self, rows, cols ):

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
        s='\n'.join([str(item) for item in self.tray])
        return s+ '\n'
        
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

        #adds the block
        for i in range(width):
            for j in range(height):
                self.tray[j+row_pos][i+col_pos] = ID
    
    
    
    def RemoveBlock(self, block):
        #this doesn't really 'delete' the Block object, it just removes it from the tray
        width=int(block.getWidth())
        height=int(block.getHeight())
        ID=block.getID()
        row_pos=int(block.getPos()[0])
        col_pos=int(block.getPos()[1])
          
        for i in range(width):
            for j in range(height):
                if int(self.tray[j+row_pos][i+col_pos]==ID):
                    self.tray[j+row_pos][i+col_pos]= 0
 
    # MoveBlock is depreciated. Each new config will result in a new Board.
    #This will be handled in Puzzle.py   
'''  
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
            moves.append("Up")
        if canMoveDown(block):
            moves.append("Down")
        if canMoveRight(block):
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

#considering moving this class to its own file        
class Block:

    _width = 0
    _height = 0
    _row_pos = 0
    _col_pos = 0
    
    def __init__(self,height, width, row_pos,col_pos, ID):

	self._width = int(width)
        self._height = int(height)
        self._row_pos = int(row_pos)
        self._col_pos = int(col_pos)
        self._ID = ID


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
    
    def getID(self):
        return self._ID

    
    '''def __str__(self):
	return ' Width: '+ str(self._width ) +\
		' Height: '+str(self._height) +\
		' Row_pos: '+str(self._row_pos) +\
		' Col_pos: '+str(self._col_pos)+'\n'

    def __repr__(self):
	return self.__str__()'''

#consider moving this to its own file, or deleteing it entirely
def test():
    b = Board(3,3)
    #print("This is a test 3x3 Board called 'b'\n")
    print(b)

    b1= Block(1,2,0,1,1)
    b.AddBlock(b1)
    #print("Add a 1x2 test block called 1\n")
    print(b)

    b2 = Block(1,1,2,0,2)
    b.AddBlock(b2)
    #print("Add a 1x1 test block called 2 \n")
    print(b)

    b3 = Block(1,2,2,1,3)
    b.AddBlock(b3)
    #print("Add a 1x2 test block called 3 \n")
    print(b)

    #print("Attempt to add a 1x1 test block called 3 to an already occupied spot\n")
    #b3= Block(1,1,0,0)
    #b.AddBlock(b3,3)
    #print(b)

    #print("Attempt to add a 1x1 test block called 4 to an out of bound spot\n")
    #b4= Block(1,1,5,5)
    #b.AddBlock(b4,4)
    #print(b)


    return b


#b= test()

