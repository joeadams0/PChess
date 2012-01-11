#*****************************************************************************************
#
#
#Joe Adams
#
#
#Discription: Defines a piece. Pieces are the objects that can move on the chessboard
#
#
#*****************************************************************************************


import Team
class Piece(object):
	def __init__(self, xpos, ypos,team, name, canLeap,fgcolor):
		self.xpos = xpos
		self.ypos = ypos
		self.team = team 
		self.name = name
		self.canLeap = canLeap
		self.fgcolor = fgcolor
		self.hasMoved = False

	def getName(self):
		return self.name
	def getTeam(self):
		return self.team.team
