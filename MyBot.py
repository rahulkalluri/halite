import hlt
from hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random
from networking import *
import sys
import numpy as np




myID, game_map = hlt.get_init()
hlt.send_init("rahulkalluri")

def zero_still(square):
	if square.strength < 6 * square.production:
		return Move(square, STILL)
	else:
		return Move(square, random.choice((NORTH, EAST, SOUTH, WEST, STILL)))

		
		
while True:
    game_map.get_frame()
    moves = [Move(square, random.choice((NORTH, EAST, SOUTH, WEST, STILL))) for square in game_map if square.owner == myID]
    hlt.send_frame(moves)
