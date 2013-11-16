import sys
from Board import *
from Block import *

hash_table = {}


def HashConfig(blocks):
    ints =[]
    key = ""
    for block in blocks:
        num=""
        for i in range(len(block)):
            num+= str(block[i])
        ints.append(int(num))        
    ints.sort()
    
    for int in ints:
        key += str(int)
    
    hash_table[key]= 'list of original configurations '+\
                        'of blocks, before being sorted'
    if key in hash_table:
        newlist = hash_table[key]
    else:
        newlist = []


    newlist.append(blocks)


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
        
    for i in range(len(raw_blocks)):
        tmp=[]
        for j in range(len(raw_blocks[i])):
            if (raw_blocks[i][j] != ' '):
                tmp.append(raw_blocks[i][j])
        b = Block(tmp[0],tmp[1],tmp[2],tmp[3],i+1)            
        blocks.append(b)

    print("\n~~~~~~first MakeBoard attempt~~~~~\n")
    board = MakeBoard(board_height, board_width, blocks)
    boardlist.append(board)    

        #for board in boardlist:
            #print(board)
            #print(board.PossibleMoves())
    print("~~~~intial blocks from file~~~:\n")
    print(blocks)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")         
    print("~~~~intial boardlist~~~~~~~~~~:\n")
    print(boardlist)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")  

    newlist =NewConfigs(boardlist)

    print("~~~~new boardlist~~~~~~~~~~~~~:\n")
    print(newlist)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n") 
    #for board in newlist:
        #print(board)
        #print(board.PossibleMoves())

def MakeBoard(height,width,blocks):
    board = Board(int(height),int(width))
    for x in range(len(blocks)):
        board.AddBlock(blocks[x])
    #return board, board.PossibleMoves(blocks), blocks
    print("~~~~~~~~~~~~~~~~~~~ MakeBoard() board: " + "\n" + str(board))
    return board
    
def NewConfigs(boardlist):
    ret_list =[]
    
    for board in boardlist:
        print("~~~~~~~~~~~~~~~~~~~~~NewConfigs() board: " + "\n" + str(board))
        moves = board.PossibleMoves()
        print("~~~~~~~~~~~~~~~~~~~~~NewConfigs() moves: " + str(moves))
        for ID in moves:
            for move in moves[ID]:
                ret_list.append(MakeNewBoard(board,ID,move))
    return ret_list


def MakeNewBoard(board,ID,move):
    print("\n~~~~~~~~~~~~~~~~~~MakeNewBoard() starts~~~~~~~~~~~~~~~~~~~\n")
    blocks = board.getBlockList()
    
    newblocklist=[]
    print("~~~~~~~~~~~~~~~~~MakeNewBoard() blocks: " + str(blocks))
    print("~~~~~~~~~~~~~~~~~MakeNewBoard() ID: "+ str(ID) + "\n")

    for block in blocks:
        print("~~~~~~~~~~~~~~~~~~MakeNewBoard() block.getID() consistency check: " + "\n" +\
        "block: " + str(block) + "\n" +\
        "ID: " +str(ID) + "\n" +\
        "block.getID(): " +str(block.getID()))

        if str(block.getID())==str(ID):
            print("~~~~~hello from the OldBlock check! Success!~~~~~~\n\n") 
            OldBlock = block

        elif str(block.getID())!=str(ID):
            print("~~~~~ entered elif block.getID()!=ID~~~~~~\n\n") 
            newblocklist.append(block)
        else:
            raise Exception("welp, this isn't working...\n")
     
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

    print("~~~~~~~~~~~~~~OldBlock properties~~~~~~~~~~~~~~~~~~ \n" +\
    "OldBlock.getHeight(): " + str(OldBlock.getHeight()) +"\n" +\
    "OldBlock.getWidth(): " + str(OldBlock.getWidth()) +"\n" +\
    "OldBlock.getPos()[0]: " + str(OldBlock.getPos()[0]) +"\n" +\
    "OldBlock.getPos()[1]: " + str(OldBlock.getPos()[1]) +"\n" +\
    "OldBlock.getID(): " + str(OldBlock.getID()))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")


    #This is where things get wonky...and why passing OldBlock.getID() to NewBlock fails...
    print("~~~~~~~~~~~OldBlock.getID(): " + str(OldBlock.getID()))
    OldID = str(OldBlock.getID)
    print("~~~~~~~OldID: " + str(OldID) +"\n")
        
    NewBlock = Block(OldBlock.getHeight(), OldBlock.getWidth(), NewRowPos,NewColPos,OldID)
    #NewBlock = OldBlock
    print("~~~~~~~~~~~~~~NewBlock properties~~~~~~~~~~~~~~~~~~ \n" +\
    "NewBlock.getHeight(): " + str(NewBlock.getHeight()) +"\n" +\
    "NewBlock.getWidth(): " + str(NewBlock.getWidth()) +"\n" +\
    "NewBlock.getPos()[0]: " + str(NewBlock.getPos()[0]) +"\n" +\
    "NewBlock.getPos()[1]: " + str(NewBlock.getPos()[1]) +"\n" +\
    "NewBlock.getID(): " + str(NewBlock.getID()))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")


    print("~~~~~~~~~~~~~MakeNewBoard() NewBlock print: " + str(NewBlock))
    newblocklist.append(NewBlock)

    print("~~~~~~~~~~~~~MakeNewBoard() newblocklist: \n")
    print(str(newblocklist) + "\n")  

    #call initial MakeBoard function
    NewBoard = MakeBoard(board._height,board._width,newblocklist)

    print("\n~~~~~~~~~~~~~~~~~~MakeNewBoard() finishes!~~~~~~~~~~~~~~~~~~~\n")
    return NewBoard
    
#assumes single block goal
def GoalCheck(Board, goal):
    '''single line goal'''
    for block in Board:
        if block.isGoal(goal):
            return True         #that's it you're done




#allows for goal cases for multiple blocks
#requires parsing of goal file
def checkGoal(Board,goal):
    '''Assuming that goal is a list'''
    goals= len(goals)
    count = 0
    for goalblock in goal:
        for block in Board:
            if block.isGoal(goalblock):
                count +=1
    if count == goals:
        return True
    else:
        return False




#the following tests the RemoveBlock() method by removing the first block added to the board
#board.RemoveBlock(blocks[0])
#print(board)




if __name__=="__main__":
    main(sys.argv)

