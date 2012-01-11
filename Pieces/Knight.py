from Piece import Piece
class Knight(Piece):
	def __init__(self, xpos, ypos,team):
		Piece.__init__(self,xpos,ypos,team, "Knight", True, None)
	
	def possibleMoves(self):
		moves =[]
		xpos = self.xpos
		ypos = self.ypos
		if self.xpos-2>=0:
			if self.ypos-1>=0:
				moves.append((ypos-1)*8+xpos-2)
			if self.ypos+1<=7:
				moves.append((ypos+1)*8+xpos-2)
		if self.xpos-1>=0:
			if self.ypos-2>=0:
				moves.append((ypos-2)*8+ xpos-1)	
			if self.ypos+2<=7:
				moves.append((ypos+2)*8 + xpos-1)
		if self.xpos+2<=7:
                        if self.ypos-1>=0:
                                moves.append((ypos-1)*8+xpos+2) 
                        if self.ypos+1<=7:
                                moves.append((ypos+1)*8+xpos+2)
                if self.xpos+1<=7:
                        if self.ypos-2>=0:
                                moves.append((ypos-2)*8+ xpos+1)
                        if self.ypos+2<=7:
                                moves.append((ypos+2)*8 + xpos+1)

		return moves
