import sys
from Board import *
from Block import *


hash_table = {}


goals = []

def SolutionNotFound(boardlist):

    tmplist = []
 
    for board in boardlist:
        count = 0
        for block in board.getBlockList():
            for GoalBlock in goals:
                if block.isequal(GoalBlock):
                    count +=1
        
        if count == len(goals):
            print(board)
            return False
    return True

def MakeHash(board):
    file_block=""
    ints =[] #a sorted list of integer representation of file_block
    hash_val = ""
    num_list= [] #a list of integer representation of file_block
    config = ""
    
    for block in board.getBlockList():
        file_block=str(block.getHeight())+str(block.getWidth())+str(block.getPos()[0])+str(block.getPos()[1])
        ints.append(int(file_block))
        num_list.append(file_block)
    ints.sort()
    
    for thing in ints:
        hash_val += str(thing)
    for thing in num_list:
        config += str(thing)
    return hash_val,config


def CheckForHash(boardlist):
    flag = 0
    for board in boardlist:
        hashtuple = MakeHash(board)
        if hashtuple[0] in hash_table:
            newlist = hash_table[key]
            if hashtuple[1] not in hash_table[key]:
                newlist.append(hashtuple[1])
            else:
                break
        else:
            newlist = []
            newlist.append(hashtuple[1])

    hash_table[key]= newlist

    


def main(argv):
    file1 = argv[1]
    file2 = argv[2]


    file1 = open(file1,'r')
    file2 = open(file2, 'r')


    lines = file1.readlines()
    goallines = file2.readlines()


    file1.close()
    file2.close()


    tray_dimensions = lines[0]
    board_height = int(tray_dimensions[0])
    board_width = int(tray_dimensions[2])


    raw_blocks = lines[1:]
    blocks=[]
    boardlist = []
        
    for i in xrange(len(raw_blocks)):
        tmp=[]
        for j in xrange(len(raw_blocks[i])):
            if (raw_blocks[i][j] != ' '):
                tmp.append(raw_blocks[i][j])
        b = Block(tmp[0],tmp[1],tmp[2],tmp[3],i+1)            
        blocks.append(b)

    for i in xrange(len(goallines)):
        tmp=[]
        for j in xrange(len(goallines[i])):
            if (goallines[i][j] != ' '):
                tmp.append(goallines[i][j])
        b = Block(tmp[0],tmp[1],tmp[2],tmp[3],i+1)            
        goals.append(b)

    board = MakeBoard(board_height, board_width, blocks)
    boardlist.append(board)    
     
    
    x = 0
    while(SolutionNotFound(boardlist)):
        x +=1
        for board in boardlist:
            hashedboard = MakeHash(board)
            key = hashedboard[0]
            
            if key in hash_table:
                newlist = hash_table[key]
                if hashedboard[1] not in hash_table[key]:
                    newlist.append(hashedboard[1])
                else:
                    boardlist.remove(board)
                    break
            else:
                newlist = []
                newlist.append(hashedboard[1])
            hash_table[key]= newlist
            
        if len(boardlist) == 0:
            print("\nNo solution can be found\n")
            sys.exit(1)
            
        boardlist = NewConfigs(boardlist)

    print("puzzle was solved in " +str(x)+ " moves")


def MakeBoard(height,width,blocks):
    board = Board(int(height),int(width))
    for x in xrange(len(blocks)):
        board.AddBlock(blocks[x])
    return board
    
def NewConfigs(boardlist):
    ret_list =[]
    
    for board in boardlist:
        moves = board.PossibleMoves()
        for ID in moves:
            for move in moves[ID]:
                ret_list.append(MakeNewBoard(board,ID,move))
    return ret_list


def MakeNewBoard(board,ID,move):
    blocks = board.getBlockList()
    
    newblocklist=[]

    for block in blocks:

        if str(block.getID())!=str(ID):
            newblocklist.append(block)
        elif str(block.getID())==str(ID):
            OldBlock = block      
        else:
            raise Exception("MakeNewBoard failed!")
    
        
    if move == "Left":
        NewRowPos =OldBlock.getPos()[0]
        NewColPos =OldBlock.getPos()[1]-1
    elif move == "Right":
        NewRowPos =OldBlock.getPos()[0]
        NewColPos =OldBlock.getPos()[1]+1
    elif move == "Up":
        NewRowPos =OldBlock.getPos()[0]-1
        NewColPos =OldBlock.getPos()[1]
    elif move == "Down":
        NewRowPos =OldBlock.getPos()[0]+1
        NewColPos =OldBlock.getPos()[1]
    else:
        raise Exception("MakeNewBoard failed!")

    newblocklist.append(Block(OldBlock.getHeight(), OldBlock.getWidth(), NewRowPos,NewColPos,OldBlock.getID()))

    #call initial MakeBoard function.
    height = board._height
    width = board._width

    return MakeBoard(height,width,newblocklist)



if __name__=="__main__":
    main(sys.argv)

