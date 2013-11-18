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
        self._ID = int(ID)



    def isequal(self,other):
  
        return (self._width == other._width) and (self._height == other._height) and (self.getPos() == other.getPos())


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


    def __str__(self):
        return str(self._ID)
    
    
    def __repr__(self):
        return self.__str__()

    


