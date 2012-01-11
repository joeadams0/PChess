#****************************************************************************************
#
#
#Joe Adams
#
#
#Discription: Class that holds the Queen Piece
#
#
#****************************************************************************************

from Piece import Piece
class Queen(Piece):
	def __init__(self,xpos,ypos,team):

		Piece.__init__(self,xpos,ypos,team, "Queen", False, None)

	def possibleMoves(self):
		moves = []
		for i in range(0,8):
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
                        if i != self.ypos:
                                moves.append(i*8+self.xpos)
                        if i != self.xpos:
                                moves.append(self.ypos*8+i)
                return moves
