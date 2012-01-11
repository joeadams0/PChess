#****************************************************************************************
#
#
#Joe Adams
#
#
#Discription: Class that holds all the moves for the Rook Piece
#
#
#****************************************************************************************


from Piece import Piece
class Rook(Piece):
	def __init__(self, xpos, ypos, team):
		Piece.__init__(self,xpos,ypos,team,"Rook", False, None)

	def possibleMoves(self):
		moves = []
		xpos = self.xpos
		ypos = self.ypos
		for i in range(0,8):
			if i != ypos:
				moves.append(i*8+xpos)
			if i != xpos:
				moves.append(ypos*8+i)
		return moves
