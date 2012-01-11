#****************************************************************************************
#
#
#Joe Adams
#
#
#Description: Defines a space on the chess board.
#
#
#****************************************************************************************


from Pieces import Team
import Tkinter
from Tkinter import *
from Pieces.Blank import Blank
from Moves import Move
class Space:
	
	def __init__(self, label, color, piece, xpos, ypos):
		self.label = label
		self.color = color
		self.piece = piece
		self.xpos = xpos
		self.ypos = ypos
	
	
	def getLabel(self):
		return self.label

	def getColor(self):
		return self.color

	def addpiece(self, piece):
                self.piece = piece
                self.label.configure(text = piece.name, fg = piece.fgcolor)
		piece.xpos = self.xpos
		piece.ypos = self.ypos

	def removepiece(self, chessboard):
		self.piece = Blank(self.xpos,self.ypos,chessboard.team3)
		self.label.configure(text= "")
	
	
#***************************************************************************************
#
#Check whether it was the first or second click. If it is the first click, it highlights #the possible moves. If it is the second click, it de-highlights the possible moves and tries to move to the space that was clicked second.
#
#****************************************************************************************

def changeState(widg,wboard,highlightedPieces,chessboard):
	
        for i in wboard:
                if i.label == widg:
                        canMove = True
                        if len(highlightedPieces)==0:
                                canMove = i.piece.team.canMove
                        if canMove:
                                firstClick(highlightedPieces, chessboard, widg,i)
        if len(highlightedPieces) == 2:
                secondClick(chessboard)
	

#Actions for first click
def firstClick(highlightedPieces,chessboard, widg,i):
        highlightedPieces.append(i)
       	posspaces = chessboard.FindPlacesToMove(i)
       	if len(highlightedPieces)==1:
       	        chessboard.posspaces = posspaces
       	        for x in posspaces:
       	                x.label.configure(bg="yellow")
	widg.configure(bg = "yellow")

#Actions for second click
def secondClick(chessboard):
        for x in chessboard.posspaces:
                x.label.configure(bg = x.color)
        move = Move(chessboard.pieces[0],chessboard.pieces[1],chessboard)
        move.TryToMove()
        chessboard.pieces[0].label.configure(bg = chessboard.pieces[0].color, relief ="sunken")
        chessboard.pieces[1].label.configure(bg = chessboard.pieces[1].color, relief = "sunken")
        chessboard.pieces = []
        chessboard.posspaces = []
	
