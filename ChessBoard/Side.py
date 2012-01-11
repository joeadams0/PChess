#****************************************************************************************
#
#
#Joe Adams
#
#
#Description: Defines a Side. A side contains 8 pawns and and two rooks, Bishops and Knights, a King and a Queen.
#
#
#****************************************************************************************
from Pieces.Piece import Piece
from Pieces.Rook import Rook
from Pieces.Knight import Knight
from Pieces.Bishop import Bishop
from Pieces.Queen import Queen
from Pieces.King import King
from Pieces.Pawn import Pawn
from Pieces.Team import Team
class Side:
	def __init__(self, team):
		self.Side = []
		self.team = team
		self.initialize()

	def initialize(self):
		team = Team(self.team)
		team.canMove = False
		self.Side.append(Rook(-1,-1,team))
		self.Side.append(Knight(-1,-1,team))
		self.Side.append(Bishop(-1,-1,team))
		self.Side.append(King(-1,-1,team))
		self.Side.append(Queen(-1,-1,team))
		self.Side.append(Bishop(-1,-1,team))
		self.Side.append(Knight(-1,-1,team))
		self.Side.append(Rook(-1,-1,team))

		for x in range(0,8):
			self.Side.append(Pawn(-1,-1,team))
		
	def getSide(self):
		return self.Side
