#****************************************************************************************
#
#
#Joe Adams
#
#
#Discription: Initializes and controls the chess board. It assigns pieces and controls the coloring of the spaces for the possible moves.
#
#
#****************************************************************************************

import Tkinter
from Tkinter import *
from Pieces.Team import Team
import SpaceClass
from SpaceClass import Space
from Pieces import Piece
from Side import Side
from Board import Board
from Pieces.Blank import Blank
from Moves import Move


class ChessBoard(Tkinter.Tk):


	def __init__(self,parent, playchess):


		Tkinter.Tk.__init__(self)

		self.parent = parent
		self.board = []
		self.pieces = []
		self.playchess = playchess
		self.posspaces = []
		self.side1 = None
		self.side2 = None
		self.team1 = None
		self.team2 = None
		self.team3 = None
		self.initialize(self.board)

	def initialize(self, board):


		self.team3 = Team(0)
		self.team3.canMove = False
		self.grid()

		side = Side(1)
		side2 = Side(2)
		self.side1 = side
		self.side2 = side2

		pieces1 = side.getSide()
		pieces2 = side2.getSide()

		self.team1 = pieces1[0].team
		self.team2 = pieces2[0].team

		self.team1.canMove = True

		self.board = Board(self).getBoard()

		for x in range(0,64):
			xpos = self.board[x].xpos
			ypos = self.board[x].ypos
			label = self.board[x].label
			if x < 16:
				self.board[x].addpiece(pieces1[x])
				pieces1[x].fgcolor = "blue"
				self.board[x].label.configure(fg = "blue") 
			elif x>= 48:
				self.board[x].addpiece(pieces2[63-x])
				pieces2[63-x].fgcolor = "red"
				self.board[x].label.configure(fg = "red")
			else:
				self.board[x].addpiece(Blank(x%8,x/8, self.team3))
			label.bind("<Button-1>", listener)
                        label.grid(column = xpos, row = ypos)




	
#******************************************************************************************
#
#Find moves:
#
#Finds all the possible places to move'
#
#
#*****************************************************************************************
	def FindPlacesToMove(self,space1):
        	piece = space1.piece
        	spaces = []
        	if piece != None:
                	moves = piece.possibleMoves()
                	for i in moves:
                        	move = Move(space1,self.board[i],self)
                        	cmove = move.canMove(True)
                        	if cmove:
                                	spaces.append(self.board[i])
        	return spaces

	
	def getSide(self,team):
		if team == 1:
			return self.side1
		if team == 2: 
			return self.side2
		return False

	def getOtherSide(self,team):
		if team == 1:
			return self.side2
		if team == 2: 
			return self.side1

def listener(event):
        widg = event.widget
	wboard = widg.master.board
	highlightedPieces = widg.master.pieces
	chessboard = widg.master
	SpaceClass.changeState(widg,wboard,highlightedPieces,chessboard)


if __name__ == "__main__":
        chessboard = ChessBoard(None,None)
        chessboard.mainloop()
