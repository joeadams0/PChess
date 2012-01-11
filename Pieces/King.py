#****************************************************************************************
#
#
#Joe Adams
#
#
#Discription: Is the Class for the King Piece
#
#
#****************************************************************************************

from Piece import Piece
class King(Piece):
	def __init__(self,xpos,ypos,team):
		Piece.__init__(self,xpos,ypos,team, "King", False, None)
	
	def possibleMoves(self):
		xpos = self.xpos
		ypos = self.ypos
		moves = []
                i = 1
                if self.xpos+i<8:
                        moves.append(ypos*8+xpos +i)
                	if self.ypos+i <8:
                            	moves.append((ypos+i)*8+xpos + i)
                        if self.ypos-i>=0:
                                moves.append((ypos-i)*8 + xpos +i)
                if self.xpos-i>=0:
                        moves.append(ypos*8+xpos-i)
                        if self.ypos+i <8:
                              	moves.append((ypos+i)*8+xpos - i)
                        if self.ypos-i>=0:
				moves.append((ypos-i)*8 + xpos -i)
		if ypos-1>=0:
                        moves.append((ypos-1)*8+xpos)
		if ypos +1<=7:
			moves.append((ypos+1)*8 +xpos)
		return moves
