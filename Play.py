#****************************************************************************************
#
#
#Joe Adams
#
#
#Discription: PlayChess runs initializes and controls the chess game. Contains the functions that control moves and possible moves.
#
#
#****************************************************************************************

from ChessBoard.ChessBoardClass import ChessBoard

class PlayChess:
	def __init__(self):
		self.chessboard = ChessBoard(None,self)
		self.chessboard.title("Chess")
		self.chessboard.mainloop()


if __name__ == "__main__":
	PlayChess()
