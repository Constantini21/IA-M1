from random import randint, choice

class HillClimbingRandom:
	MAX_SIDE_STEPS = 30 # número máximo de ciclos pelos quais o solver passará onde o valor heurístico não diminui
	
	def __init__(self, num_queens):
		self.num_queens = num_queens
		self.set_new_board()
	
	def set_new_board(self):
		"""Configura um novo tabuleiro e redefine todas as variáveis ​​relevantes."""

		self.board = [randint(0, self.num_queens - 1) for i in range(self.num_queens)]
		self.side_steps = 0 # número de ciclos o menor valor heurístico não muda
		self.last_heuristic_value = self.get_num_attacks(self.board)
	
	def print_board(self, board):
		"""Imprime uma representação visual do tabuleiro."""

		for i in range(len(board)):
			for j in range(len(board)):
				if (len(board) - i) - 1 - board[j] == 0:
					print('[Q]', end='')
				else:
					print('[ ]', end='')
				
				if (j == (len(board) - 1)):
					print('')
			print
	
	def get_num_attacks(self, board):
		"""Retorna o número total de pares de rainhas que podem se atacar no tabuleiro."""

		num_attacks = 0
		
		# iterar através de todas as rainhas
		for i in range(len(board)):
			queen_row = board[i]
			
			# compara com outras rainhas
			for j in range(len(board)):
				if board[j] == queen_row and i != j:
					num_attacks += 1
				
				if board[j] == (j - i) + queen_row and i != j:
					num_attacks += 1
				
				if board[j] == -(j - i) + queen_row and i != j:
					num_attacks += 1
		
		return num_attacks / 2

	def get_move_heuristic(self, move):
		"""Retorna o valor heurístico de um tabuleiro modificado, criada por meio de movimentação.
			move = tupla com [0] como col para mudar, [1] como novo valor col"""

		if move[1] == self.board[move[0]]: # retorna o valor heurístico atual
			return self.last_heuristic_value
		
		move_heuristic = self.last_heuristic_value
		cur_queen_row = self.board[move[0]]

		for i in range(self.num_queens):
			# remover colisões da posição atual da rainha
			if self.board[i] == cur_queen_row and i != move[0]: # horizontal
				move_heuristic -= 1
			elif self.board[i] == (i - move[0]) + cur_queen_row and i != move[0]: # diagonal, left-bottom->top-right
				move_heuristic -= 1
			elif self.board[i] == -(i - move[0]) + cur_queen_row and i != move[0]: # diagonal, top-left->bottom-right
				move_heuristic -= 1
			
			# adiciona colisões para a nova posição da rainha
			if self.board[i] == move[1] and i != move[0]: # horizontal
				move_heuristic += 1
			elif self.board[i] == (i - move[0]) + move[1] and i != move[0]: # diagonal, left-bottom->top-right
				move_heuristic += 1
			elif self.board[i] == -(i - move[0]) + move[1] and i != move[0]: # diagonal, top-left->bottom-right
				move_heuristic += 1
		
		return move_heuristic
	
	def make_next_move(self):
		"""Muda o tabuleiro para um novo tabuleiro com menor valor heurístico encontrado na configuração atual;
			se nenhum valor heurístico inferior for encontrado, escolhe o tabuleiro aleatório de valores heurísticos de igual valor."""
		
		# obtém valores heurísticos de todos os locais de movimentos possíveis
		best_heuristic_value = self.last_heuristic_value

		# contém todas as próximas configurações com valores heurísticos iguais
		best_moves = [(0, self.board[0])]
		
		# passa por todos os pontos do tabuleiro para encontrar o próximo valor heurístico mais baixo
		for i in range(len(self.board)):
			for j in range(len(self.board)):
				if j != self.board[i]:
					cur_heuristic = self.get_move_heuristic((i, j))
					if cur_heuristic < best_heuristic_value:
						best_heuristic_value = cur_heuristic
						best_moves = [(i, j)]
					elif cur_heuristic == best_heuristic_value:
						best_moves.append((i, j))
		
		# se nenhuma heurística inferior for encontrada, incrementa self.side_steps
		if best_heuristic_value == self.last_heuristic_value:
			self.side_steps += 1
		
		# selecione a próxima configuração aleatoriamente a partir de valores heurísticos iguais
		selected_move = choice(best_moves)
		self.board[selected_move[0]] = selected_move[1]
		self.last_heuristic_value = best_heuristic_value
	
	def solve(self):
		"""Chama make_next_move() até que uma solução seja encontrada ou self.side_steps >= MAX_SIDE_STEPS."""
		while self.last_heuristic_value > 0:
			# se estiver no limite de passos laterais, inicie um novo tabuleiro
			if self.side_steps >= HillClimbingRandom.MAX_SIDE_STEPS:
				print('Falha ao achar uma solução. criando novo tabuleiro...')
				self.set_new_board()
			
			self.make_next_move()
