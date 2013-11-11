import sys
from Tray import *


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





file1 = sys.argv[1]
file2 = sys.argv[2]


file1 = open(file1,'r')

lines = file1.readlines()

tray_dimensions = lines[0]

board_height = tray_dimensions[0]

board_width = tray_dimensions[2]

board = Board(int(board_height),int(board_width))

print(board)
raw_blocks = lines[1:]
blocks=[]





for i in range(len(raw_blocks)):
    tmp=[]
    for j in range(len(raw_blocks[1])):
        if (raw_blocks[i][j] != ' '):
	    tmp.append(raw_blocks[i][j])
    b = Block(tmp[0],tmp[1],tmp[2],tmp[3])	    
    blocks.append(b)

file1.close()

#print(b.getHeight())

for x in range(len(blocks)):
    board.AddBlock(blocks[x])
print(board)

#the following tests the RemoveBlock() method by removing the first block added to the board
#board.RemoveBlock(blocks[0])
#print(board)




