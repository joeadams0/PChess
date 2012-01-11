#****************************************************************************************
#
#
#Joe Adams
#
#
#Description: Controls the moving of pieces around the board. 
#
#
#****************************************************************************************
from Tkinter import *
import tkMessageBox
import ChessBoard.SpaceClass 
#A Move has a start space and a target space a boolean canMove
class Move():

	def __init__(self, space1,space2,chessboard):
		self.startSpace = space1
		self.endSpace = space2
		self.cMove = False
		self.chessboard = chessboard

	def execute(self):
		chessboard = self.chessboard
		if(self.canMove):
			self.endSpace.addpiece(self.startSpace.piece)
			self.startSpace.removepiece(chessboard)
			chessboard.team2.canMove = not chessboard.team2.canMove
        		chessboard.team1.canMove = not chessboard.team1.canMove
	
	#Checks if the move is possible by checking every space in between the spaces recursively.
	# Pawns and knights have special cases 
 	def canMove(self,isFirstCheck):
		space1 = self.startSpace
		space2 = self.endSpace
                piece1 = space1.piece
                piece2 = space2.piece
                xpos1 = piece1.xpos
                ypos1 = piece1.ypos
                xpos2 = piece2.xpos
                ypos2 = piece2.ypos
		chessboard = self.chessboard
		board = self.chessboard.board

                s1 = id(space1)
                s2 = id(space2)
                if s1 == s2:
                	return True
                if piece1.getTeam() == piece2.getTeam():
                        return False
		
		#special checks for pawn
                if piece1.name == "Pawn":
                        if piece2.getTeam()!=0:
                                if piece2.xpos ==piece1.xpos:
                                        return False
                                return True
                        else:
                                if piece1.xpos != piece2.xpos:
                                        return False
                                if piece1.getTeam()==1:
                                        if piece1.ypos == piece2.ypos-2:
                                                if piece1.hasMoved == False:
							move = Move(space1,board[(ypos2-1)*8+xpos2],chessboard)
                                                        return move.canMove(False)
                                        if piece1.ypos == piece2.ypos-1:
                                                return True
                                if piece1.getTeam() ==2:
                                        if piece1.ypos == piece2.ypos+2:
                                                if piece1.hasMoved == False:
							move = Move(space1,board[(ypos2+1)*8+xpos2],chessboard)
                                                        return move.canMove(False)
                                        if piece1.ypos == piece2.ypos+1:
                                                return True
                        return False
                
		if piece1.canLeap:
                        return True
		
		
		#checks whether space2 is occupied if its not the first check
		if not isFirstCheck:
			if space2.piece.team != chessboard.team3:
				return False;

	
                if ypos1== ypos2:

			#if space1 is directly to the left of space2, check all spaces in between
                        if xpos1<xpos2:
				move = Move(space1,board[ypos1*8+xpos2-1],chessboard)
                                return move.canMove(False)
			#if space1 is directly to the right of space2, check all spaces in between
                        elif xpos1>xpos2:
				move = Move(space1,board[ypos1*8+xpos2+1],chessboard)
                                return move.canMove(False)
                elif xpos1==xpos2:
			
			#if space1 is directly above space2, check all spaces in between
                        if ypos1<ypos2:
				move = Move(space1,board[(ypos2-1)*8+xpos1],chessboard)
                                return move.canMove(False)
			#if space1 is directly below space two, check all spaces in between
                        if ypos2<ypos1:
				move = Move(space1,board[(ypos2+1)*8+xpos1],chessboard)
                                return move.canMove(False)
                else:
                        if xpos1<xpos2:
				
				#if space1 is diagnally left and up from space 2, 
				#check all spaces in between
                                if ypos1<ypos2:
					move = Move(space1,board[(ypos2-1)*8+xpos2-1],chessboard)
                                        return move.canMove(False)
				#if space1 is diaganally left and below space 2, 
				# check all spaces in between
                                elif ypos2<ypos1:
					move = Move(space1,board[(ypos2+1)*8+xpos2-1],chessboard)
                                        return move.canMove(False)
                        elif xpos2<xpos1:

				#if space1 is diagonally to the right and above space2,
				#check spaces in between
                                if ypos1<ypos2:
					move = Move(space1,board[(ypos2-1)*8+xpos2+1],chessboard)
                                        return move.canMove(False)
				#if space1 is diagonally to the right and below space2,
				#check spaces in between
                                elif ypos2<ypos1:
					move = Move(space1,board[(ypos2+1)*8+xpos2+1],chessboard)
                                        return move.canMove(False)
                return True

	
	#Tries to execute move, but if can move is false, it does not execute
	def TryToMove(self):
		space1 = self.startSpace
		piece = space1.piece
		space2 = self.endSpace
               	if space1 != space2:
                        if piece != None:
                               	moves = piece.possibleMoves()
                               	for i in moves:
                                       	if space2.ypos*8+space2.xpos == i:
                                               	canmove = self.canMove(True)
                                               	if canmove:
                                                       	if space1!=space2:
                                                               	piece.hasMoved = True
                                                       	self.cMove = True;
                                                       	self.execute()



		


