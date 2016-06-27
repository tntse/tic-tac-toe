
from __future__ import print_function

class Game(object):

	def __init__(self):
		self.board = None
		self.player1 = "X"
		self.player2 = "O"
		self.winner = None
		self.lastMove = None

	def newGame(self):
		self.board = [[None, None, None], 
					  [None, None, None], 
					  [None, None, None]]
		self.winner = None
		self.lastMove = None
		return
	
	def play(self):
		keepPlaying = True

		while(keepPlaying):
			self.startGame()

			if(self.winner == None):
				print("\nIt's a tie!")
			else:
				print ("Congrats! The ", end="")
				print(self.winner, end="")
				print("'s win the game!")

			self.displayBoard()

			response = raw_input("Play Again? [Y/N]: ")
			if(response == 'N' or response == 'n'):
				keepPlaying = False
			else:
				self.player1 = "X" if self.player1 == "O" else "O"
				self.player2 = "X" if self.player2 == "O" else "O"
		return


	def startGame(self):
		print ("Welcome to Text based Tic-Tac-Toe!")
		print ("Match 3 in Row to win!")
		
		self.newGame()
		turn = "X"
		print ("Player ", end="")
		print (1 if (self.player1 == "X") else 2, end="")
		print (" Starts. \n")

		while(self.winner == None and not self.isBoardFull()):
			success = False

			while(not success):
				print("Player ", end="")
				print(1 if (self.player1 == turn) else 2, end="")
				print(" Turn.")
				self.displayBoard()
				print ("Enter move coordinates: ")
				x = int(input("Enter row: "))
				y = int(input("Enter column: "))
				success = self.isLegalMove(x, y)

				if(success):
					self.move(turn, x, y)
					turn = self.player2 if turn == self.player1 else self.player1
					print("")
				else:
					print ("\nInvalid move, please try again: ")
		return


	def move (self, marker, x, y):
		self.lastMove = [x, y]
		self.board[x][y] = marker

		if( self.isWinner(marker)):
			self.winner = marker
		return


	def isBoardFull(self):
		return not (None in self.board[0]) and not (None in self.board[1]) and not (None in self.board[2])

	def isWinner(self, marker):

		x = self.lastMove[0]
		y = self.lastMove[1]

		# check row
		if(self.board[x][0] == self.board[x][1] == self.board[x][2] == marker):
			return True

		# check column
		if(self.board[0][y] == self.board[1][y] == self.board[2][y] == marker):
			return True

		# check diagonals
		if(x == y):
			if(self.board[0][0] == self.board[1][1] == self.board[2][2] == marker):
				return True

			if(self.board[0][2] == self.board[1][1] == self.board[2][0] == marker):
				return True

		return False

	def isLegalMove(self, x, y):
		if( (0 <= x <= 2) and (0 <= y <= 2)):
			if(self.board[x][y] == None):
				return True
		return False

	def displayBoard(self):
		print ("\033[4m", end="")
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				if(self.board[i][j] == None):
					print (" - ", end="")
				else:
					print (' ' + self.board[i][j], end=" ")

				if(j < len(self.board[i])-1):
					print ("|", end="")

			if(i==len(self.board)-2):
				print ("\033[0m")
			else:
				print ("")

if __name__ == "__main__":
	game = Game()
	game.play()