#****************************************************************************************
#
#
#Joe Adams
#
#
#Discription: Creates a Chess Board, but does not assign pieces
#
#
#****************************************************************************************


from Tkinter import Label
from SpaceClass import Space
from Pieces import Piece
class Board:
	def __init__(self, parent):
		self.board = []
		labelparent = parent
		test = False
		for x in range(0,8):
                        if x%2 == 0:
                                test = True
                        if x%2 == 1:
                                test = False
                        for i in range(0,8):
                                if test:
                                        if i%2 ==0:
                                                label2 = Label(parent, fg = "white", height = 2, width = 6, bg = "black", relief = "sunken")
                                                space = Space(label2, "black", None,i,x)
                                        if i%2 == 1:
                                                label2 = Label(parent, fg = "black", height = 2, width = 6, bg = "white", relief = "sunken")
                                                space = Space(label2, "white",None,i,x)
                                else:
                                        if i%2 ==0:
                                                label2 = Label(parent, fg = "black", height = 2, width = 6, bg = "white", relief = "sunken")
                                                space = Space(label2, "white",None,i,x)
                                        if i%2 == 1:
                                                label2 = Label(parent, fg = "white", height = 2, width = 6, bg = "black", relief = "sunken")
                                                space = Space(label2, "black",None,i,x)
                                self.board.append(space)
	

	def getBoard(self):
		return self.board

