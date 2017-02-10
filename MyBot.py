import hlt
from hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random
from networking import *
import sys
import numpy as np




myID, game_map = hlt.get_init()
hlt.send_init("rahulkalluri")

def zero_still(square):

	#only attack if neighbor is weaker than our current piece
	for direction, neighbor in enumerate(game_map.neighbors(square)):
		if neighbor.owner != myID and neighbor.strength < square.strength:
			return Move(square, direction)
	
	#only move if the strength is more than a certain value
	if square.strength < 6 * square.production:
		return Move(square, STILL)
		
	else:
		#remove randomness of blocks moving, since that's inefficient
		return Move(square, random.choice(SOUTH, EAST)))

		
		
while True:
    game_map.get_frame()
	
    moves = [zero_still(square) for square in game_map if square.owner == myID]
    hlt.send_frame(moves)
