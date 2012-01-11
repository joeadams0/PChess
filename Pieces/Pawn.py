#****************************************************************************************
#
#
#Joe Adams
#
# 
#Discription: Holds all the moves for the Pawn Piece. 
#
#
#****************************************************************************************


from Piece import Piece
class Pawn(Piece):
	def __init__(self, xpos, ypos, team):
		Piece.__init__(self,xpos,ypos, team, "Pawn", False, None)
	
	def possibleMoves(self):
		moves = []
		if self.hasMoved== False:
			if self.getTeam() == 1:
				moves.append((self.ypos+2)*8+self.xpos)
			if self.getTeam() == 2:
				moves.append((self.ypos-2)*8+self.xpos)
		if self.getTeam() ==2:
			moves.append((self.ypos-1)*8+self.xpos-1)
			moves.append((self.ypos-1)*8+self.xpos)
			moves.append((self.ypos-1)*8+self.xpos+1)
		elif self.getTeam() ==1:
			moves.append((self.ypos+1)*8+self.xpos+1)
			moves.append((self.ypos+1)*8+self.xpos)
			moves.append((self.ypos+1)*8+self.xpos-1)
		return moves

	
		 
