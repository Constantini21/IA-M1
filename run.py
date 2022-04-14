import sys
import nQueens
from time import time

if __name__ == '__main__':
	# certifique-se de que um número de rainhas para colocar no tabuleiro foi passado
	if len(sys.argv) < 2:
		print('Este programa requer um número de rainhas para colocar como argumento.')
		print('Exemplo: python run.py 8')
		sys.exit(1)
	
	try:
		num_queens = int(sys.argv[1])
	except ValueError:
		print('Valor passado é invalido.')
	
	solvers = []	
	solvers.append(getattr(nQueens, 'HillClimbingRandom')(num_queens))
	
	for solver in solvers:
		print('Procurando solução com {}...'.format(solver.__class__.__name__))
		start_time = time()
		solver.solve()
		print('Solução encontrada em {}s:'.format(round(time() - start_time, 4)))
		solver.print_board(solver.board)
