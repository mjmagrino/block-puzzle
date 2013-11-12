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



def main(argv):
	file1 = sys.argv[1]
	file2 = sys.argv[2]

	file1 = open(file1,'r')
	file2 = open(file2, 'r')

	lines = file1.readlines()
	goal = file2.readlines()

	file1.close()
	file2.close()

	tray_dimensions = lines[0]
	board_height = tray_dimensions[0]
	board_width = tray_dimensions[2]

	raw_blocks = lines[1:]
	blocks=[]
	for i in range(len(raw_blocks)):
    	tmp=[]
		for j in range(len(raw_blocks[1])):
        	if (raw_blocks[i][j] != ' '):
	    	tmp.append(raw_blocks[i][j])
    	b = Block(tmp[0],tmp[1],tmp[2],tmp[3])	    
    	blocks.append(b)

	board = MakeBoard(board_height, board_width, blocks)
    print(board)
    print(board.PossibleMoves(blocks))


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


def GoalCheck(Board, goal):
    for block in Board:
        if block.isGoal(goal):
            return True         #that's it you're done
        


#the following tests the RemoveBlock() method by removing the first block added to the board
#board.RemoveBlock(blocks[0])
#print(board)


if __name__=="__main__":
    main(sys.argv)


