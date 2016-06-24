
class Game(object):

	def __init__(self):
		self.board = None
		self.player1 = "X"
		self.player2 = "O"
		self.winner = None
		self.lastMove = None

	def newGame(self):
		self.board = [[None] * 3] * 3
		self.winner = None
		self.lastMove = None
	
	def play(self):
		keepPlaying = true

		while(keepPlaying):
			self.startGame()
			print "Congrats! The " + self.winner + "'s win the game!\n"
			print "Play Again?\n "
			response = input("Play Again? [Y/N]: ")
			if(response == "N" or response == "n"):
				keepPlaying = false
			else:
				self.player1 = "X" if self.player1 == "O" else "O"
				self.player2 = "X" if self.player2 == "O" else "O"
		return


	def startGame(self):
		print "Welcome to Text based Tic-Tac-Toe!\n"
		print "Match 3 in Row to win!\n"
		
		newGame()
		turn = "X"
		print "Player ", 1 if (self.player1 == "X") else 2, " Starts.\n"

		while(self.winner == None):
			success = false
			self.displayBoard()

			while(not success):
				print "Enter move coordinates: \n"
				x = int(input("Enter row: "))
				y = int(input("Enter column: "))
				success = self.isLegalMove(x, y)

				if(success):
					self.move(turn, x, y)
					turn = self.player2 if turn == self.player1 else player1
				else:
					print "Invalid move, please try again: \n"
		return


	def move (self, marker, x, y):
		self.lastMove = [x, y]
		self.board[x][y] = marker

		if( self.isWinner()):
			self.winner = marker
		return


	def isWinner(self):

		x = self.lastMove[0]
		y = self.lastMove[1]

		# check row
		if(self.board[x][0] == self.board[x][1] == self.board[x][2]):
			return true

		# check column
		if(self.board[0][y] == self.board[1][y] == self.board[2][y]):
			return true

		# check diagonals
		if(x == y):
			if(self.board[0][0] == self.board[1][1] == self.board[2][2]):
				return true

			if(self.board[0][2] == self.board[1][1] == self.board[2][0]):
				return true

		return false

	def isLegalMove(self, x, y):
		if( (0 <= x <= 1) and (0 <= y <= 2)):
			if(self.board[x][y] == None):
				return true
		return false

	def displayBoard(self):
		for i in range(3):
			for j in range(3):
				if(self.board[i][j] == None):
					print "-"
				else:
					print self.board[i][j]

				if(j < 2):
					print " | "
			print "\n"