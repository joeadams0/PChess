#****************************************************************************************
#
#
#Joe Adams
#
#
#Discription: Is a class for a blank piece to take empty spaces
#
#
#****************************************************************************************

from Piece import Piece
import Team

class Blank(Piece):

	def __init__(self,xpos,ypos, team):
		Piece.__init__(self,xpos,ypos, team, None, False,None)
	
	def possibleMoves(self):
		return []	
