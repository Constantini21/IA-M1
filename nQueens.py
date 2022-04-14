from random import randint, choice
from chessBoard import Board

class HillClimbingRandom:
	MAX_SIDE_STEPS = 30 # número máximo de ciclos pelos quais o solver passará onde o valor heurístico não diminui
	
	def __init__(self, numQueens):
		self.numQueens = numQueens
		self.setNewBoard()
		self.chessBoard = Board(numQueens)		
	
	def setNewBoard(self):
		"""Configura um novo tabuleiro e redefine todas as variáveis ​​relevantes."""

		self.board = [randint(0, self.numQueens - 1) for i in range(self.numQueens)]
		self.sideSteps = 0
		self.lastHeuristicValue = self.getNumAttacks()
	
	def printBoard(self):
		"""Imprime uma representação visual do tabuleiro."""
		self.chessBoard.resetBoard()

		for i in range(len(self.board)):			
			for j in range(len(self.board)):
				if (len(self.board) - i) - 1 - self.board[j] == 0:
					self.chessBoard.boardState[i][j] = 'queen'
					print('[Q]', end='')
				else:
					print('[ ]', end='')
					self.chessBoard.boardState[i][j] = None
				
				if (j == (len(self.board) - 1)):
					print('')
			print

		self.chessBoard.show()
	
	def getNumAttacks(self):
		"""Retorna o número total de pares de rainhas que podem se atacar no tabuleiro."""

		numAttacks = 0
		
		# iterar através de todas as rainhas
		for i in range(len(self.board)):
			queenRow = self.board[i]
			
			# compara com outras rainhas
			for j in range(len(self.board)):
				if self.board[j] == queenRow and i != j:
					numAttacks += 1
				
				if self.board[j] == (j - i) + queenRow and i != j:
					numAttacks += 1
				
				if self.board[j] == -(j - i) + queenRow and i != j:
					numAttacks += 1
		
		return numAttacks / 2

	def getMoveHeuristic(self, move):
		"""Retorna o valor heurístico, criada por meio da movimentação."""

		if move[1] == self.board[move[0]]: # retorna o valor heurístico atual
			return self.lastHeuristicValue
		
		moveHeuristic = self.lastHeuristicValue
		curQueenRow = self.board[move[0]]

		for i in range(self.numQueens):
			# remover colisões da posição atual da rainha
			if self.board[i] == curQueenRow and i != move[0]: # horizontal
				moveHeuristic -= 1
			elif self.board[i] == (i - move[0]) + curQueenRow and i != move[0]: # diagonal, left-bottom->top-right
				moveHeuristic -= 1
			elif self.board[i] == -(i - move[0]) + curQueenRow and i != move[0]: # diagonal, top-left->bottom-right
				moveHeuristic -= 1
			
			# adiciona colisões para a nova posição da rainha
			if self.board[i] == move[1] and i != move[0]: # horizontal
				moveHeuristic += 1
			elif self.board[i] == (i - move[0]) + move[1] and i != move[0]: # diagonal, left-bottom->top-right
				moveHeuristic += 1
			elif self.board[i] == -(i - move[0]) + move[1] and i != move[0]: # diagonal, top-left->bottom-right
				moveHeuristic += 1
		
		return moveHeuristic
	
	def makeNextMove(self):
		"""Move para uma nova casa no tabuleiro com menor valor heurístico encontrado
			se nenhum valor heurístico inferior for encontrado, escolhe uma casa aleatório com valores heurísticos de igual valor."""
		
		bestHeuristicValue = self.lastHeuristicValue

		# todas as próximas configurações com valores heurísticos iguais
		bestMoves = [(0, self.board[0])]
		
		# passa por todas as casas do tabuleiro para encontrar o menor valor heurístico
		for i in range(len(self.board)):
			for j in range(len(self.board)):
				if j != self.board[i]:
					curHeuristic = self.getMoveHeuristic((i, j))
					if curHeuristic < bestHeuristicValue:
						bestHeuristicValue = curHeuristic
						bestMoves = [(i, j)]
					elif curHeuristic == bestHeuristicValue:
						bestMoves.append((i, j))
		
		# se nenhuma heurística inferior for encontrada, incrementa self.sideSteps
		if bestHeuristicValue == self.lastHeuristicValue:
			self.sideSteps += 1
		
		# selecione a próxima configuração aleatoriamente a partir de valores heurísticos iguais
		moveSelected = choice(bestMoves)
		self.board[moveSelected[0]] = moveSelected[1]
		self.lastHeuristicValue = bestHeuristicValue
	
	def solve(self):
		"""makeNextMove() até que uma solução seja encontrada"""
		while self.lastHeuristicValue > 0:
			# se atingir o maximo de tentativas, inicie um novo tabuleiro
			if self.sideSteps >= HillClimbingRandom.MAX_SIDE_STEPS:
				print('Falha ao encontrar uma solução. criando novo tabuleiro...')
				self.setNewBoard()
			
			self.makeNextMove()
