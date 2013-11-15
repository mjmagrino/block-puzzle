import sys
from Board import *


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

	boardlist.append(MakeBoard(board_height, board_width, blocks))
    print(boardlist[0][0])
    print(boardlist[0][0].PossibleMoves(blocks))

    newlist=[]
    for thing in boardslist:
        for ID in thing[1]:
            for move in thing[1][ID]:
                newlist.append(MakeNewBoard(thing[0],blocks,ID,move))
    print('\n')
    for board in newlist:
        print(board[0])
        print(board[0].PossibleMoves(board[2]))
        print('\n')


def MakeBoard(height,width,blocks):
    board = Board(int(height),int(width))
    for x in range(len(blocks)):
        board.AddBlock(blocks[x])
    return board

def NewConfigs(boardlist,blocks):
    ret_list =[]
    for board in boardlist:
        moves = board.PossibleMoves(block)
        for ID in moves:
            for move in moves[ID]:
                ret_list.append(MakeNewBoard(board,blocks,ID,move))
    return ret_list

def MakeNewBoard(board, blocks,ID,move):
    blocklist=[]

    for block in blocks:
        if block.getID()!=ID:
            blocklist.append(block)
        else:
            OldBlock = block
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

    NewBlock = Block(OldBlock.getHeight(), OldBlock.getWidth(), NewRowPos,NewColPos,OldBlock.getID)

    blocklist.append(NewBlock)

    #call intial MakeBoard function
    NewBoard = MakeBoard(board._height,board._width,blocklist)


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


