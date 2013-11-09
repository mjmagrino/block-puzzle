import sys
from Tray import *


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
    block_attr=[]
    for j in range(len(raw_blocks[1])):
        if (raw_blocks[i][j] != ' '):
	    block_attr.append(raw_blocks[i][j])
    b = Block(block_attr[0],block_attr[1],block_attr[2],block_attr[3])	    
    blocks.append(b)

file1.close()

print(b.getHeight())

for x in range(len(blocks)):
    board.AddBlock(blocks[x])
print(board)




