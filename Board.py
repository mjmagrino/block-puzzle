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

           
    def AddBlock(self,width,height,ID,row_pos,col_pos):
            """
            necessary modifications:
            AddBlock() needs to take as input a file of type Block
            width and height need to be taken into account when propigating
            the Block across the positions that it takes up
            """

            """ Are we going to have ID's?
            He was saying that they'll screw things up,
            so how do we know what blocks occupy what spaces?
            I might be confused. I think I remember him saying
            making them global in the beginning would be fine.
            """

        #checks to see if block can be added. borders accounted for?
        for i in range(width):
            for j in range(height):
                if int (self.tray[i+row_pos][j+col_pos]) !=0:
                    raise Exception('Block cannot be added at: ', i+row_pos,j+col_pos)

        #adds the block
        for i in range(width):
            for j in range(height):
                self.tray[i+row_pos][j+col_pos] = ID

        

    def PossibleMoves(self):
         '''every block may have possible moves
          so in order to make this list, go through each block
           on the board and find possible moves for it

            sum of moves for each block
            '''
         
    def PossibleBlockMoves(self,block):
        '''is there space above it, right, left, below? '''
         
                   
    """Need to figure out what we will use to store possible moves for a block.
    'moves' is a non-existant list right now"""
    def canMoveLeft(self,block):

        pos = block.getPos()
        i = pos[0]
        j = pos[1]
        h= block.getHeight()
        w = block.getWidth()
        count = 0
        for a in range(h):
            if int(matrix[i+a][j-1]) == 0:
                count +=1
        if count == h:
            moves.append('Left')
        
    def canMoveRight(self,block)

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
            moves.append('Right')

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
            moves.append('Up')
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
            moves.append('Down')
        return len(moves)
        
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
  
        return (self._width == other._width) && (self._height == other._height)

    def getSize(self):
        return self.getHeight(),self.getWidth()

    def getPos(self):
        return self._row_pos,self._col_pos

    def getHeight(self):
        return self._height

    def getWidth(self):
        return self._width

