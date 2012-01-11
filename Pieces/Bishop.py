#*****************************************************************************************
#
#
#Joe Adams
#
#
#Discription: Holds all move sfor the bishop piece
#
#
#*****************************************************************************************

from Piece import Piece
class Bishop(Piece):
	def __init__(self, xpos,ypos, team):
		Piece.__init__(self,xpos,ypos,team, "Bishop", False, None)

	def possibleMoves(self):
		moves = []
		xpos = self.xpos
		ypos = self.ypos
		for i in range(1,8):
                        if self.xpos+i<8:
                                if self.ypos+i <8:
                                         moves.append((self.ypos+i)*8+self.xpos + i)
                                if self.ypos-i>=0:
                                        moves.append((self.ypos-i)*8 + self.xpos +i)
                        if self.xpos-i>=0:
                                if self.ypos+i <8:
                                         moves.append((self.ypos+i)*8+self.xpos - i)
                                if self.ypos-i>=0:
                                        moves.append((self.ypos-i)*8 + self.xpos -i)

		return moves
